"""Self-improving memory layer for the AppWorld agent.

Two cooperating stores:

* ``LocalSkillStore`` - instant, deterministic on-disk cache of distilled
  skills/lessons (Markdown + a JSONL index). Always available, even with no
  network or API key. This is what makes within-run skill reuse work.
* ``HydraMemory`` - thin, defensive wrapper over the HydraDB SDK that mirrors
  skills into HydraDB ``knowledge`` and lessons into HydraDB ``memory`` and does
  semantic/graph recall. Degrades to a no-op if the SDK or key is missing or any
  call fails, so the agent never breaks.

``SkillMemory`` is the facade the agent and scripts use: it stores to both and
recalls from both, merging + de-duplicating results.

Design rules (from the plan):
* Skills are HINTS, AppWorld API docs are the source of truth.
* Never store secrets (passwords, access tokens, JWTs) in any store.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Iterable, Optional

try:  # load .env so the module works standalone and inside scripts
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parent / ".env")
except Exception:
    pass

# ---------------------------------------------------------------------------
# config
# ---------------------------------------------------------------------------
MEMORY_DIR = Path(os.environ.get("MEMORY_DIR", Path(__file__).resolve().parent / "memory"))
SKILLS_DIR = MEMORY_DIR / "skills"
INDEX_PATH = MEMORY_DIR / "index.jsonl"

HYDRA_TENANT_ID = os.environ.get("HYDRA_TENANT_ID", "appworld_agentathon")
HYDRA_SUB_TENANT = os.environ.get("HYDRA_SUB_TENANT", "dev")
HYDRA_API_KEY = (
    os.environ.get("HYDRA_DB_API_KEY")
    or os.environ.get("HYDRADB_API_KEY")
    or os.environ.get("HYDRA_API_KEY")
)
# When set, recall returns only eval-verified knowledge (outcome pass/fail),
# never unverified in-run "completed" captures. Prevents memory poisoning.
MEMORY_VERIFIED_ONLY = os.environ.get("MEMORY_VERIFIED_ONLY", "1") != "0"
HYDRA_MODE = os.environ.get("HYDRA_RECALL_MODE", "fast")  # fast | accurate
HYDRA_TIMEOUT = float(os.environ.get("HYDRA_TIMEOUT", "20"))
HYDRA_TENANT_WAIT = float(os.environ.get("HYDRA_TENANT_WAIT", "180"))  # max wait for async provisioning
HYDRA_POLL_INTERVAL = float(os.environ.get("HYDRA_POLL_INTERVAL", "5"))

_STOPWORDS = {
    "the", "a", "an", "and", "or", "to", "of", "in", "on", "for", "with", "my",
    "me", "is", "are", "be", "that", "this", "it", "as", "at", "by", "from",
    "i", "you", "your", "their", "them", "then", "if", "all", "any", "into",
    "list", "show", "get", "give", "tell", "find", "please", "want", "need",
}


# ---------------------------------------------------------------------------
# secret scrubbing
# ---------------------------------------------------------------------------
_JWT_RE = re.compile(r"eyJ[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+")
_KV_SECRET_RE = re.compile(
    r"(?i)([\"']?(?:password|passwd|pwd|access[_-]?token|token|api[_-]?key|secret|"
    r"client[_-]?secret|authorization|bearer)[\"']?\s*[:=]\s*)"
    r"(\"[^\"]*\"|'[^']*'|[^\s,}\)]+)"
)


def scrub_secrets(text: str) -> str:
    """Redact credentials so nothing sensitive is ever persisted."""
    if not text:
        return text
    text = _JWT_RE.sub("<redacted-token>", text)
    text = _KV_SECRET_RE.sub(r"\1<redacted>", text)
    return text


def _tokens(text: str) -> set[str]:
    words = re.findall(r"[a-zA-Z0-9_]+", (text or "").lower())
    return {w for w in words if len(w) > 2 and w not in _STOPWORDS}


# ---------------------------------------------------------------------------
# skill model
# ---------------------------------------------------------------------------
@dataclass
class Skill:
    title: str
    apps: list[str] = field(default_factory=list)
    task_type: str = "answer"          # answer | mutation | mixed
    when_to_use: str = ""
    procedure: str = ""                # numbered API flow / approach
    pitfalls: list[str] = field(default_factory=list)
    verification: list[str] = field(default_factory=list)
    answer_shape: str = ""
    outcome: str = "pass"              # pass | fail | completed
    source_task_id: str = ""
    source_experiment: str = ""
    tags: list[str] = field(default_factory=list)
    skill_id: str = ""
    created_at: float = 0.0

    def __post_init__(self) -> None:
        if not self.skill_id:
            self.skill_id = self.compute_id()
        if not self.created_at:
            self.created_at = time.time()
        # scrub everything that can hold free text
        self.procedure = scrub_secrets(self.procedure)
        self.when_to_use = scrub_secrets(self.when_to_use)
        self.pitfalls = [scrub_secrets(p) for p in self.pitfalls]
        self.verification = [scrub_secrets(v) for v in self.verification]

    def compute_id(self) -> str:
        key_words = [w for w in _tokens(self.title) ]
        sig = "|".join(sorted(self.apps)) + "|" + self.task_type + "|" + "_".join(sorted(key_words)[:6])
        return hashlib.sha1(sig.encode("utf-8")).hexdigest()[:12]

    @property
    def kind(self) -> str:
        return "lesson" if self.outcome == "fail" else "skill"

    def to_markdown(self) -> str:
        lines = [f"# {self.title}", ""]
        lines.append(f"- apps: {', '.join(self.apps) or 'unknown'}")
        lines.append(f"- task_type: {self.task_type}")
        lines.append(f"- outcome: {self.outcome}")
        if self.source_task_id:
            lines.append(f"- source_task: {self.source_task_id}")
        lines.append("")
        if self.when_to_use:
            lines += ["## When to use", self.when_to_use, ""]
        if self.procedure:
            lines += ["## Procedure", self.procedure, ""]
        if self.pitfalls:
            lines += ["## Pitfalls"] + [f"- {p}" for p in self.pitfalls] + [""]
        if self.verification:
            lines += ["## Verification"] + [f"- {v}" for v in self.verification] + [""]
        if self.answer_shape:
            lines += ["## Answer shape", self.answer_shape, ""]
        return "\n".join(lines).strip() + "\n"

    def searchable_text(self) -> str:
        return " ".join(
            [self.title, " ".join(self.apps), self.task_type, self.when_to_use,
             " ".join(self.tags), self.procedure]
        )


# ---------------------------------------------------------------------------
# local store
# ---------------------------------------------------------------------------
class LocalSkillStore:
    def __init__(self) -> None:
        SKILLS_DIR.mkdir(parents=True, exist_ok=True)
        self._index: dict[str, dict] = {}
        self._load()

    def _load(self) -> None:
        if not INDEX_PATH.exists():
            return
        for line in INDEX_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                self._index[rec["skill_id"]] = rec
            except Exception:
                continue

    def _flush(self) -> None:
        with INDEX_PATH.open("w", encoding="utf-8") as fh:
            for rec in self._index.values():
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

    def add(self, skill: Skill) -> dict:
        md = skill.to_markdown()
        (SKILLS_DIR / f"{skill.skill_id}.md").write_text(md, encoding="utf-8")
        rec = {
            "skill_id": skill.skill_id,
            "title": skill.title,
            "apps": skill.apps,
            "task_type": skill.task_type,
            "outcome": skill.outcome,
            "tags": skill.tags,
            "source_task_id": skill.source_task_id,
            "source_experiment": skill.source_experiment,
            "created_at": skill.created_at,
            "search": skill.searchable_text().lower(),
            "markdown": md,
        }
        self._index[skill.skill_id] = rec  # upsert
        self._flush()
        return rec

    def search(self, query: str, k: int = 3, apps_hint: Iterable[str] = ()) -> list[dict]:
        q_tokens = _tokens(query)
        apps_hint = {a.lower() for a in apps_hint}
        scored: list[tuple[float, dict]] = []
        for rec in self._index.values():
            # verified-only mode: skip unverified in-run captures entirely
            if MEMORY_VERIFIED_ONLY and rec.get("outcome") not in {"pass", "fail"}:
                continue
            rec_tokens = _tokens(rec.get("search", ""))
            if not rec_tokens:
                continue
            overlap = len(q_tokens & rec_tokens)
            if overlap == 0 and not (apps_hint & {a.lower() for a in rec.get("apps", [])}):
                continue
            score = float(overlap)
            if apps_hint & {a.lower() for a in rec.get("apps", [])}:
                score += 2.0
            # prefer eval-verified knowledge over unverified in-run captures
            outcome = rec.get("outcome")
            if outcome == "pass":
                score += 1.5   # verified-correct recipe
            elif outcome == "fail":
                score += 0.75  # verified failure -> valuable warning
            # outcome == "completed" (unverified capture): no boost
            scored.append((score, rec))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [rec for _, rec in scored[:k]]

    def all(self) -> list[dict]:
        return list(self._index.values())


# ---------------------------------------------------------------------------
# HydraDB wrapper (defensive)
# ---------------------------------------------------------------------------
class HydraMemory:
    def __init__(
        self,
        tenant_id: str = HYDRA_TENANT_ID,
        sub_tenant_id: str = HYDRA_SUB_TENANT,
        api_key: Optional[str] = HYDRA_API_KEY,
    ) -> None:
        self.tenant_id = tenant_id
        self.sub_tenant_id = sub_tenant_id
        self.api_key = api_key
        self._client = None
        self._tenant_ready = False
        self._warned = False
        self.enabled = bool(api_key)
        if self.enabled:
            try:
                from hydra_db import HydraDB  # noqa: F401
            except Exception as exc:  # SDK not installed
                self._warn(f"hydra_db import failed ({exc}); HydraDB disabled")
                self.enabled = False

    # -- helpers ------------------------------------------------------------
    def _warn(self, msg: str) -> None:
        # rate-limited but not permanently muted, so repeated failures stay visible
        self._warn_count = getattr(self, "_warn_count", 0) + 1
        if self._warn_count <= 8:
            print(f"  [hydra] {msg}")

    @staticmethod
    def _is_provisioning_error(exc: Exception) -> bool:
        s = str(exc).upper()
        return "TENANT_NOT_FOUND" in s or "NOT_READY" in s or "NOT PROVISIONED" in s

    def _get_client(self):
        if self._client is None:
            from hydra_db import HydraDB
            self._client = HydraDB(token=self.api_key, timeout=HYDRA_TIMEOUT)
        return self._client

    def _infra_ready(self, client) -> bool:
        try:
            resp = client.tenants.status(tenant_id=self.tenant_id)
            infra = getattr(getattr(resp, "data", None), "infra", None)
            return bool(getattr(infra, "ready_for_ingestion", False))
        except Exception:
            return False

    def ensure_tenant(self) -> bool:
        if not self.enabled:
            return False
        if self._tenant_ready:
            return True
        try:
            client = self._get_client()
            try:
                client.tenants.create(tenant_id=self.tenant_id, is_embeddings_tenant=False)
            except Exception as exc:
                # already-exists is fine; anything else we log once
                if "exist" not in str(exc).lower() and "409" not in str(exc):
                    self._warn(f"tenant create note: {exc}")
            # tenant provisioning is asynchronous; poll until infra is ready
            deadline = time.time() + HYDRA_TENANT_WAIT
            while time.time() < deadline:
                if self._infra_ready(client):
                    self._tenant_ready = True
                    return True
                time.sleep(HYDRA_POLL_INTERVAL)
            self._warn(
                f"tenant '{self.tenant_id}' not ready after {HYDRA_TENANT_WAIT}s; "
                "skipping HydraDB this run (it will likely be ready next run)"
            )
            return False
        except Exception as exc:
            self._warn(f"ensure_tenant failed ({exc}); HydraDB disabled")
            self.enabled = False
            return False

    # -- writes -------------------------------------------------------------
    def _ingest_with_retry(self, fn) -> bool:
        try:
            fn()
            return True
        except Exception as exc:
            if self._is_provisioning_error(exc):
                # status said ready but the collection lagged; wait once and retry
                self._tenant_ready = False
                if self.ensure_tenant():
                    try:
                        fn()
                        return True
                    except Exception as exc2:
                        self._warn(f"ingest retry failed ({exc2})")
                        return False
            self._warn(f"ingest failed ({exc})")
            return False

    def ingest_skill(self, skill: Skill) -> bool:
        if not self.ensure_tenant():
            return False
        client = self._get_client()
        md = skill.to_markdown().encode("utf-8")
        # one metadata object per document, as a JSON array
        meta = json.dumps([{
            "apps": ",".join(skill.apps),
            "task_type": skill.task_type,
            "outcome": skill.outcome,
            "source_task_id": skill.source_task_id,
            "tags": ",".join(skill.tags),
        }])

        def _do():
            client.context.ingest(
                tenant_id=self.tenant_id,
                type="knowledge",
                upsert=True,
                documents=[(f"{skill.skill_id}.md", md, "text/markdown")],
                document_metadata=meta,
            )

        return self._ingest_with_retry(_do)

    def ingest_lesson(self, skill: Skill) -> bool:
        if not self.ensure_tenant():
            return False
        client = self._get_client()
        text = f"{skill.title}\n{skill.to_markdown()}"
        memories = json.dumps([{"text": scrub_secrets(text), "infer": False}])

        def _do():
            client.context.ingest(
                tenant_id=self.tenant_id,
                type="memory",
                sub_tenant_id=self.sub_tenant_id,
                memories=memories,
            )

        return self._ingest_with_retry(_do)

    # -- reads --------------------------------------------------------------
    def recall(self, query: str, k: int = 3) -> list[dict]:
        if not self.enabled:
            return []
        if not self.ensure_tenant():
            return []
        out: list[dict] = []
        try:
            client = self._get_client()
            resp = client.query(
                tenant_id=self.tenant_id,
                query=query,
                max_results=k,
                mode=HYDRA_MODE,
                graph_context=True,
            )
            chunks = getattr(getattr(resp, "data", None), "chunks", None) or []
            for ch in chunks:
                content = getattr(ch, "chunk_content", None)
                if not content:
                    continue
                out.append({
                    "text": content,
                    "title": getattr(ch, "source_title", "") or "",
                    "score": getattr(ch, "relevancy_score", None),
                    "source": "hydra",
                })
        except Exception as exc:
            self._warn(f"recall failed ({exc})")
        return out


# ---------------------------------------------------------------------------
# facade
# ---------------------------------------------------------------------------
class SkillMemory:
    def __init__(self, use_hydra: bool = True) -> None:
        self.local = LocalSkillStore()
        self.hydra = HydraMemory() if use_hydra else HydraMemory(api_key=None)

    @property
    def hydra_enabled(self) -> bool:
        return self.hydra.enabled

    def store(self, skill: Skill) -> None:
        self.local.add(skill)
        if skill.outcome == "fail":
            self.hydra.ingest_lesson(skill)
        else:
            self.hydra.ingest_skill(skill)

    @staticmethod
    def _content_key(text: str) -> str:
        norm = re.sub(r"\s+", " ", (text or "").strip().lower())[:160]
        return hashlib.sha1(norm.encode("utf-8")).hexdigest()

    def recall(self, query: str, k: int = 3, apps_hint: Iterable[str] = ()) -> list[str]:
        """Return up to k formatted skill blocks (Hydra-first, then local)."""
        blocks: list[str] = []
        seen: set[str] = set()

        for hit in self.hydra.recall(query, k=k):
            text = hit.get("text", "").strip()
            if not text:
                continue
            key = self._content_key(text)
            if key in seen:
                continue
            seen.add(key)
            blocks.append(text)

        if len(blocks) < k:
            for rec in self.local.search(query, k=k, apps_hint=apps_hint):
                md = rec.get("markdown", "").strip()
                if not md:
                    continue
                key = self._content_key(md)
                if key in seen:
                    continue
                seen.add(key)
                blocks.append(md)
                if len(blocks) >= k:
                    break
        return blocks[:k]


# ---------------------------------------------------------------------------
# self-test CLI: python appworld_memory.py --selftest
# ---------------------------------------------------------------------------
def _selftest() -> int:
    print(f"HYDRA key present: {bool(HYDRA_API_KEY)} | tenant={HYDRA_TENANT_ID} | sub={HYDRA_SUB_TENANT}")
    mem = SkillMemory()
    print(f"Hydra enabled: {mem.hydra_enabled}")
    demo = Skill(
        title="selftest spotify top-n genre ranking",
        apps=["spotify"],
        task_type="answer",
        when_to_use="A connectivity self-test skill; safe to delete.",
        procedure="1. login 2. gather library 3. sort by play_count 4. answer top N",
        pitfalls=["This is a self-test record."],
        verification=["Ignore in production."],
        source_task_id="selftest",
        tags=["selftest"],
    )
    mem.store(demo)
    print(f"Stored skill {demo.skill_id} locally + (hydra={mem.hydra_enabled}).")
    if mem.hydra_enabled:
        print("Waiting for HydraDB indexing (best-effort, up to 30s)...")
        time.sleep(5)
    hits = mem.recall("spotify top songs by play count", k=3, apps_hint=["spotify"])
    print(f"Recalled {len(hits)} block(s):")
    for i, h in enumerate(hits, 1):
        print(f"--- block {i} ---")
        print(h[:300])
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        raise SystemExit(_selftest())
    print("appworld_memory: import this module, or run with --selftest")

# HydraDB Agent Arena

Autonomous AppWorld agent for `://agent_arena`. The agent reads a supervisor
task, writes Python code against AppWorld APIs, verifies its answer or mutation,
and completes the task with `apis.supervisor.complete_task(...)`.

## What We Added

- Provider/model routing: `MODEL`, `ROUTER_MODEL`, `SOLVER_MODEL`,
  `ERROR_MODEL`, `VERIFIER_MODEL`, and `DISTILLER_MODEL` accept
  `provider/model` strings. The default target is OpenRouter Llama 3.3 70B:
  `openrouter/meta-llama/llama-3.3-70b-instruct`.
- OpenAI-compatible backends: OpenRouter, Groq, OpenAI, Anthropic, and the
  legacy Azure Llama backend are routed from one agent loop.
- HydraDB memory: successful and failed trajectories can be distilled into
  reusable skills/lessons with `scripts/extract_trajectories.py`. Runtime recall
  injects verified memory hints while treating live AppWorld API docs as the
  source of truth.
- Verified-only memory by default: in-run captures are off unless explicitly
  enabled, which avoids poisoning future tasks with unverified completions.
- Solver prompt improvements: the agent now emphasizes schema inspection,
  credential/login patterns, lowercase app namespaces, exact answer shape, and
  concise evidence before completion.
- Completion verifier: answer tasks are checked before submission for empty or
  guessed answers, missing evidence, suspicious counts, bad top-N shape, and
  ignored errors.
- Pagination, inspection, and ranking safeguards: prompts tell the solver to
  exhaust paginated list APIs, print sample keys before reading fields, fetch
  authoritative detail records for ranking metrics, and deduplicate entities.
- Relative-date handling: the AppWorld task datetime is injected and must be used
  for "today", "this year", "last month", and similar relative dates.
- Mutation completeness: payment/message/create/update tasks are prompted to
  include exact amounts, recipients, titles, notes, descriptions, dates, and
  follow-up messages before completion.

## Setup

Use Python 3.11.

```bash
bash setup.sh
source .venv/bin/activate
cp .env.example .env
```

Add your OpenRouter key to `.env`:

```bash
OPENROUTER_API_KEY=...
MODEL=openrouter/meta-llama/llama-3.3-70b-instruct
```

If OpenRouter changes the slug, set:

```bash
OPENROUTER_LLAMA_MODEL=meta-llama/llama-3.3-70b-instruct
```

Other supported examples:

```bash
MODEL=groq/llama-3.3-70b-versatile
MODEL=openai/gpt-5.4-mini
MODEL=anthropic/claude-opus-4-8
MODEL=azure-llama
```

## Run And Evaluate

Short development smoke test:

```bash
export APPWORLD_EXPERIMENT=team_openrouter_smoke
export APPWORLD_DATASET=dev
export MAX_TASKS=3
python agent.py
appworld evaluate team_openrouter_smoke dev
```

Official organizer eval set:

```bash
mkdir -p data/datasets
cp eval/agent_arena_eval.txt data/datasets/agent_arena_eval.txt
export APPWORLD_EXPERIMENT=team_<name>
export APPWORLD_DATASET=agent_arena_eval
export MAX_TASKS=0
python agent.py
appworld evaluate team_<name> agent_arena_eval
```

See `EVAL.md` and `SUBMISSION.md` for the organizer-provided eval set and
submission format.

## HydraDB Memory Workflow

Enable HydraDB by adding a key to `.env`:

```bash
HYDRA_DB_API_KEY=...
ENABLE_MEMORY=1
MEMORY_VERIFIED_ONLY=1
```

After a run, distill verified trajectories into the local memory cache and
HydraDB:

```bash
python scripts/extract_trajectories.py --experiment team_<name> --dataset dev
```

Use `--no-llm` for deterministic extraction, or `--dry-run` to inspect what would
be stored. The script scrubs secrets before persisting skills.

## Repo Hygiene

Do not commit `.env`, API keys, `memory/`, `memory_backup_*`, probe scripts,
terminal logs, caches, or local AppWorld outputs unless they are the exact
official submission artifacts requested by organizers.

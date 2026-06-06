──────────────────────────────── Overall Stats ─────────────────────────────────
Num Passed Tests : 8
Num Failed Tests : 2
Num Total  Tests : 10
──────────────────────────────────── Passes ────────────────────────────────────
>> Passed Requirement
assert answers match.
>> Passed Requirement
assert model changes match splitwise.Expense, splitwise.ExpenseShare,
splitwise.Notification,
ignoring file_system.Directory, file_system.File.
>> Passed Requirement
obtain added, updated, removed splitwise.Expense records using
models.changed_records,
and assert 0 were updated or removed.
>> Passed Requirement
assert all added expenses have group_id matching private_data.group_id.
>> Passed Requirement
assert all added expenses have payer_id of private_data.splitwise_user_id.
>> Passed Requirement
assert expense_description_to_amount obtained from added expenses
match the private_data.expense_description_to_amount.
>> Passed Requirement
obtain added, updated, removed splitwise.ExpenseShare records using
models.changed_records,
and assert 0 were updated or removed.
>> Passed Requirement
assert all added expense shares have expense_id matching the added expenses.
──────────────────────────────────── Fails ─────────────────────────────────────
>> Failed Requirement
assert member_ids from added expense shares from all unique expenses match
private_data.member_ids.
```python
with test(
    """
    assert member_ids from added expense shares from all unique expenses match
    private_data.member_ids.
    """
):
    expense_to_member_ids = dict_list_of(added_expense_shares, "expense_id",
"debtor_id")
    list_of_member_ids = list(expense_to_member_ids.values())
```
----------
AssertionError:  [40, 46] == [40, 46, 90]

In right but not left:
[90]

Original values:
[40, 46] == [90, 40, 46]
>> Failed Requirement
assert user_id_to_debt_amounts from added expense shares match
private_data.user_id_to_debt_amounts.
```python
with test(
    """
    assert user_id_to_debt_amounts from added expense shares match
    private_data.user_id_to_debt_amounts.
    """
):
    user_id_to_debt_amounts = defaultdict(list)
    for share in added_expense_shares:
```
----------
AssertionError:
{40: [58.5 ± 0.51, 73.0 ± 0.51, 76.5 ± 0.51, 82.0 ± 0.51, 93.0 ± 0.51, 100.0 ±
0.51], 46: [58.5 ± 0.51, 73.0 ± 0.51, 76.5 ± 0.51, 82.0 ± 0.51, 93.0 ± 0.51,
100.0 ± 0.51]}
==
{90: [39.0 ± 0.51, 48.67 ± 0.51, 51.0 ± 0.51, 54.67 ± 0.51, 62.0 ± 0.51, 66.67 ±
0.51], 40: [39.0 ± 0.51, 48.67 ± 0.51, 51.0 ± 0.51, 54.67 ± 0.51, 62.0 ± 0.51,
66.67 ± 0.51], 46: [39.0 ± 0.51, 48.67 ± 0.51, 51.0 ± 0.51, 54.67 ± 0.51, 62.0 ±
0.51, 66.67 ± 0.51]}

Original values:
{40: [58.5, 73.0, 76.5, 82.0, 93.0, 100.0], 46: [58.5, 73.0, 76.5, 82.0, 93.0,
100.0]}
==
{90: [39.0, 48.67, 51.0, 54.67, 62.0, 66.67], 40: [39.0, 48.67, 51.0, 54.67,
62.0, 66.67], 46: [39.0, 48.67, 51.0, 54.67, 62.0, 66.67]}
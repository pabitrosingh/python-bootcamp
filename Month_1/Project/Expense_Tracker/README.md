# Month 1 project - Expense Tracker

Build a menu-driven program to record and review expenses for one run of the program.

This guided project uses a list to hold expenses and a dictionary for each expense's description and amount. Month 2 teaches these data structures in detail; here, use the provided shape and focus on input, decisions, loops, functions, and calculations.

The menu uses the `match`/`case` statement, which requires Python 3.10 or newer.

## Requirements

- Start with an empty list of expenses.
- Repeat a menu until the user chooses to quit.
- Let the user add an expense with a non-empty description and a positive amount.
- Let the user view all recorded expenses.
- Let the user view the total of all recorded expenses.
- Reject blank descriptions, non-numeric amounts, and amounts that are zero or negative with a helpful message.
- Format monetary amounts to two decimal places.
- Keep expenses in memory; they do not need to be saved after exit.

## Run and test

From this directory, run:

```bash
python expense_tracker.py
python -m unittest -v
```

## Acceptance checklist

- [ ] Add multiple expenses and list each with its description and amount.
- [ ] The total equals the sum of all recorded expenses; an empty list totals `$0.00`.
- [ ] Blank descriptions, invalid text, zero, and negative amounts do not add a record.
- [ ] Unknown menu choices show a helpful message.
- [ ] Choosing quit exits cleanly.
- [ ] All automated tests pass.

## Suggested record shape

Each expense is a dictionary with a description and amount, for example:

```python
{"description": "Bus fare", "amount": 2.50}
```

The list contains one dictionary per expense. You can add records with `expenses.append(expense)` and visit them with `for expense in expenses:`.

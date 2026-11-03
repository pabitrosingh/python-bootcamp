# Mini project - ATM Simulator

Build a command-line ATM that performs one selected transaction on a starting balance. This week's version does not need a repeating menu; that is a good Week 3 extension.

## Requirements

- Start with a balance of `$100.00`.
- Display a one-time menu: check balance, deposit, or withdraw.
- Use an `if`/`elif`/`else` ladder to select the action.
- For a deposit or withdrawal, ask for an amount.
- Reject amounts that are zero or negative.
- Reject withdrawals larger than the balance.
- Show the updated balance to two decimal places after a valid transaction.
- Show a helpful message for an unknown action.

## Acceptance checklist

- [ ] Each action uses a clear conditional branch.
- [ ] Invalid amounts do not change the balance.
- [ ] A failed withdrawal leaves the balance unchanged.
- [ ] Test balance check, valid deposit, valid withdrawal, too-large withdrawal, zero, negative, and unknown action.

This project assumes numeric input. Add invalid-text handling after completing Week 4.

**Optional extension:** If using Python 3.10 or newer, try expressing the action selection with `match`/`case`. Keep the amount and balance checks as `if` conditions.

## Run

From this directory, run:

```bash
python atm_simulator.py
```

Run the automated acceptance checks with:

```bash
python -m unittest -v
```

# Project - Banking Application

Build a small in-memory banking domain model. The project practices classes, encapsulation, invariants, composition, and focused unit tests. It does not connect to a real bank or store data between runs.

The reference implementation is [`banking.py`](./banking.py); acceptance tests are in [`test_banking.py`](./test_banking.py).

## Features

- Open and look up accounts by unique account number
- Deposit and withdraw positive `Decimal` amounts
- Reject invalid amounts and withdrawals that exceed the available balance
- Transfer between two distinct accounts
- Record timestamped transactions using timezone-aware UTC datetimes
- Keep account state behind methods and expose a read-only transaction history

## Run

From the repository root:

```bash
python -m Month_3.Week_1.Project.banking
python -m unittest -v Month_3.Week_1.Project.test_banking
```

Use `Decimal` or strings for money values rather than binary floating-point numbers.

## Acceptance checklist

- [ ] A new account starts at zero unless an opening balance is supplied.
- [ ] Negative opening balances and non-positive transaction amounts are rejected.
- [ ] A failed withdrawal leaves the balance unchanged.
- [ ] A transfer updates both accounts and cannot target the same account.
- [ ] Transaction timestamps are timezone-aware.
- [ ] All tests pass.

## Extensions

- Add a daily withdrawal limit as a separate policy.
- Persist transactions to JSON in a later project; do not put file handling inside the account model.
- Add a CLI that catches domain exceptions and presents useful messages.

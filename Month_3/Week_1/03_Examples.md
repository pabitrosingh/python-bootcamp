# Week 1 / Example 3 - Protect object invariants

An account balance should not become negative. Keep its state behind methods that enforce the rule:

```python
class Account:
    def __init__(self, opening_balance=0):
        if opening_balance < 0:
            raise ValueError("opening balance cannot be negative")
        self._balance = opening_balance

    @property
    def balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount
```

`@property` lets callers read `account.balance` while keeping the update rule in `withdraw`. The underscore in `_balance` communicates that it is an implementation detail; Python does not enforce private access. Python's name mangling for names such as `__balance` is also not a security boundary.

**Try it:** Add `deposit` and reject zero or negative amounts. Write down the balance invariant before coding.

# Week 3 / Example 2 - Domain exceptions and exception chaining

Give callers a specific error when an operation violates a domain rule:

```python
class InsufficientFundsError(ValueError):
    """Raised when an account cannot cover a withdrawal."""


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
    if amount > balance:
        raise InsufficientFundsError("balance is too low")
    return balance - amount
```

When adapting a lower-level failure, retain its cause:

```python
def load_settings(path):
    try:
        return path.read_text(encoding="utf-8")
    except OSError as error:
        raise RuntimeError(f"could not read settings from {path}") from error
```

Callers can catch `InsufficientFundsError` specifically; the chained `OSError` remains visible in the traceback.

**Try it:** Add an `AccountNotFoundError` and decide whether it should derive from `LookupError` or `ValueError`, explaining the choice.

# Week 4 / Example 2 - Strategy

A strategy packages one interchangeable calculation behind a common operation:

```python
from typing import Protocol


class ShippingStrategy(Protocol):
    def cost(self, weight: float) -> float: ...


class StandardShipping:
    def cost(self, weight):
        return 5.0 + weight


class ExpressShipping:
    def cost(self, weight):
        return 12.0 + 2 * weight


class Checkout:
    def __init__(self, shipping):
        self.shipping = shipping

    def total(self, subtotal, weight):
        return subtotal + self.shipping.cost(weight)
```

`Checkout` depends on the small behavior `cost`, not on a specific shipping class. The standard library's `Protocol` describes this structural interface for type checkers; no inheritance is required at runtime.

**Try it:** Add a free-shipping strategy and test all strategies with the same `Checkout` class.

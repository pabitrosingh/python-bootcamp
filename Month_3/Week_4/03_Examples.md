# Week 4 / Example 3 - Factory and Repository

A small factory centralizes which concrete strategy to create:

```python
def make_shipping(method):
    if method == "standard":
        return StandardShipping()
    if method == "express":
        return ExpressShipping()
    raise ValueError(f"unknown shipping method: {method}")
```

A repository isolates storage operations:

```python
class InMemoryOrders:
    def __init__(self):
        self._orders = {}

    def save(self, order):
        self._orders[order.order_id] = order

    def get(self, order_id):
        return self._orders[order_id]
```

A service that receives a repository can be tested with this in-memory implementation. A future database repository can implement the same operations without changing the service. This does not make data persistent; the in-memory mapping disappears when the process ends.

**Try it:** Add `list_all()` and test that saving an order makes it retrievable by its identifier.

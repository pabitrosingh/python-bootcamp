# Exercise 3 - Composition

Create an `Order` class that owns a list of line items and a `ReceiptFormatter` class that produces a printable summary. Pass the formatter into an `OrderService` instead of inheriting from it.

**Test:** Use a fake formatter that records its input. Confirm the service passes the correct order.

**Try next:** Add a second formatter without changing the order model.

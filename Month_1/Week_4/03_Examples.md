# Week 4 / Example 3 - Local scope

A variable created inside a function is local to that function.

```python
def calculate_total(price, quantity):
    total = price * quantity
    return total


order_total = calculate_total(4.50, 3)
print(f"Total: ${order_total:.2f}")
```

`total` exists only while `calculate_total` runs; the caller receives its value through `return`. Prefer passing information in and returning results rather than changing global variables.

```python
def make_message(name):
    greeting = f"Hello, {name}!"
    return greeting


message = make_message("Sam")
print(message)
```
# Week 2 / Example 1 - Separate responsibilities

A class that reads a file, parses it, calculates totals, and formats a report has several reasons to change. Separate those responsibilities behind small functions:

```python
def calculate_total(prices):
    return sum(prices)


def format_total(total):
    return f"Total: ${total:.2f}"
```

A caller can load prices separately, pass them to `calculate_total`, and format the result. This illustrates the Single Responsibility principle. A related Open/Closed approach is to accept a callable for a variable policy rather than adding a branch for every future option:

```python
def total_with(prices, discount):
    return discount(sum(prices))


def no_discount(amount):
    return amount
```

Do not split code into tiny units without a practical reason; cohesion and clarity matter more than class count.

**Try it:** Separate the calculation from display in a report program and test the calculation without capturing terminal output.

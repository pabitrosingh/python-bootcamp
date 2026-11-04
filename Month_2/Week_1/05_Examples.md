# Week 1 / Example 5 - Tuples and unpacking

A tuple is an ordered, immutable sequence. A comma creates a tuple; parentheses are often used for clarity.

```python
point = (4, 7)
origin = 0, 0
single_item = ("Python",)  # the comma is required

x, y = point
print(x, y)  # 4 7
```

Tuples work well for fixed records whose positions have clear meaning. For a record with many fields, a dictionary can be more descriptive.

```python
book = ("The Left Hand of Darkness", "Ursula K. Le Guin", 1969)
title, author, year = book
print(f"{title} by {author} ({year})")
```

Tuple immutability means `point[0] = 5` is invalid. If a tuple contains a list, that nested list can still be mutated; immutability applies to the tuple's references, not every object reachable from it.

**Try it:** Return a `(minimum, maximum)` tuple from a list of numbers and unpack it at the call site.
# Week 1 / Example 5 - Data classes

Use `@dataclass` when a class primarily stores related data:

```python
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


first = Point(2, 3)
second = Point(2, 3)
print(first)           # Point(x=2, y=3)
print(first == second) # True
```

The decorator generates methods such as `__init__`, `__repr__`, and `__eq__` using annotated fields. An annotation is not runtime validation: `Point("left", "up")` is still constructible unless you add checks. Use `field(default_factory=...)` for a new mutable value per instance:

```python
from dataclasses import dataclass, field


@dataclass
class Team:
    members: list[str] = field(default_factory=list)
```

**Try it:** Define a `Book` data class with a title, author, and page count. Add validation if a non-positive page count is invalid for your use case.

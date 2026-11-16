# Week 1 / Example 5 - Generator expressions and exhaustion

A generator expression is a compact way to create a lazy iterator:

```python
squares = (number * number for number in range(5))

print(next(squares))  # 0
print(list(squares))  # [1, 4, 9, 16]
print(list(squares))  # []
```

The first call to `next()` consumes the value `0`. Converting `squares` to a list consumes the remaining values. Iterators do not rewind automatically; create a new generator expression when the data needs to be traversed again.

Use a list comprehension instead when you need a reusable in-memory collection or need to inspect values more than once.

**Try it:** Use `sum()` with a generator expression to total the squares from 1 through 100 without first creating a list.
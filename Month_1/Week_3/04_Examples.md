# Week 3 / Example 4 - Nested loops

A loop inside another loop is useful when each item in one group must be paired with each item in another.

```python
for row in range(1, 4):
    for column in range(1, 4):
        print(f"{row} x {column} = {row * column}")
    print("---")
```

The inner loop completes all three columns before the outer loop moves to its next row. Nested loops multiply the amount of work, so use them only when the problem needs that structure.

Try changing the ranges to print a 2-by-4 grid of coordinate pairs.
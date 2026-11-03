# Week 4 / Example 2 - Parameters and return values

Use `return` to send a result back to the caller. A returned value can be stored, printed, or passed to another function.

```python
def calculate_average(first_score, second_score, third_score):
    return (first_score + second_score + third_score) / 3


average = calculate_average(80, 90, 100)
print(f"Average: {average:.1f}")
```

A function that prints a result is useful for display. A function that returns a result is easier to reuse in more than one place.

```python
def is_passing(score):
    return score >= 60


print(is_passing(72))  # True
```
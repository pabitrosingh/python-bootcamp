# Week 1 / Example 3 - Iterate, search, and build results

Iterate over values directly when an index is not needed:

```python
temperatures = [18, 22, 16, 25]
warm_days = []

for temperature in temperatures:
    if temperature >= 20:
        warm_days.append(temperature)

print(warm_days)  # [22, 25]
```

Use `enumerate()` when the position and value are both useful:

```python
for day_number, temperature in enumerate(temperatures, start=1):
    print(f"Day {day_number}: {temperature} C")
```

Membership with `in` answers whether a value occurs in a list. `count(value)` counts occurrences, and `index(value)` returns the first matching position or raises `ValueError`.

Avoid removing items from a list while iterating over that same list: shifting positions can make elements get skipped. Build a new list instead.

**Try it:** Given a list of words, build a second list containing only words longer than four characters.
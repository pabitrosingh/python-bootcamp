# Week 2 / Example 3 - `if`/`elif`/`else` ladder

An `if`/`elif`/`else` ladder tests conditions from top to bottom and runs only the suite belonging to the first true condition. There can be several `elif` branches, and the final `else` is optional.

```python
score = 84

if score < 0 or score > 100:
    grade = "Invalid score"
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
```

The order matters: a score of 95 is also at least 80. Checking the highest threshold first ensures it receives an A. The first branch rejects values outside the expected score range instead of treating a negative score as an F.

For two outcomes, `if` and `else` alone are enough:

```python
temperature = 18

if temperature >= 20:
    print("Warm")
else:
    print("Cool")
```

For decisions inside decisions, see [Example 5: nested conditions](./05_Nested_Conditionals.md).
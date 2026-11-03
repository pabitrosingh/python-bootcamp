# Week 2 / Example 6 - Conditional expressions

A conditional expression chooses between two values and evaluates to one of them:

```python
age = 17
message = "Adult" if age >= 18 else "Minor"
print(message)
```

Read it as: “use `"Adult"` if `age >= 18`; otherwise use `"Minor"`.” Its general form is:

```python
value_if_true if condition else value_if_false
```

It is an expression, so it can be used where a value is expected:

```python
score = 72
result = "pass" if score >= 60 else "retry"
print(f"Result: {result}")
```

Use a regular `if`/`else` statement when either branch needs multiple statements or when the condition and choices are hard to understand on one line. Avoid chaining conditional expressions inside one another; a clear ladder is easier to maintain.

## Try it

1. Set `is_raining` to `True` or `False`.
2. Use a conditional expression to choose `"Bring an umbrella"` or `"No umbrella needed"`.
3. Predict the output for both values before running the code.

See the official [conditional expression reference](https://docs.python.org/3/reference/expressions.html#conditional-expressions).

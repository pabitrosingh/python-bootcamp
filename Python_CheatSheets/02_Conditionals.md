# Conditionals Cheat Sheet

Quick reference for [Month 1, Week 2: decisions and Boolean logic](../Month_1/Week_2/Week_2_Topics.md).

## Comparisons

Comparisons produce `True` or `False`.

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `<`, `<=` | Less than; less than or equal to |
| `>`, `>=` | Greater than; greater than or equal to |

```python
0 <= score <= 100  # chained comparison
```

## `if` / `elif` / `else`

Python checks branches from top to bottom and executes only the first matching branch. Put range thresholds in the right order.

```python
if score < 0 or score > 100:
    grade = "Invalid"
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
```

`elif` and the final `else` are optional; an `if` statement must have an `if` branch.

## Combine conditions

```python
is_member = True
order_total = 60

if is_member and order_total >= 50:
    print("Discount applies")

if is_member or order_total >= 50:
    print("At least one condition is true")

if not is_member:
    print("Not a member")
```

- `and`: both conditions must be true.
- `or`: at least one condition must be true.
- `not`: reverses a truth value.

Python short-circuits Boolean expressions: `and` stops at the first false operand; `or` stops at the first true operand.

```python
if denominator != 0 and 10 / denominator > 1:
    print("Safe to evaluate the quotient condition")
```

Empty strings and numeric zero are false in a condition; non-empty strings (including `"False"`) are true. Compare yes/no text explicitly.

## Nested conditions

Use a nested `if` when a second decision depends on an earlier one:

```python
if order_total >= 50:
    if is_member:
        discount_rate = 0.10
    else:
        discount_rate = 0.05
else:
    discount_rate = 0.0
```

For alternatives at the same level, an `elif` ladder is often clearer. Keep indentation consistent so each `else` belongs to the intended `if`.

## Conditional expression

For a short choice between two values:

```python
status = "Pass" if score >= 60 else "Retry"
```

General form: `value_if_true if condition else value_if_false`. Prefer a regular statement if a branch has multiple steps or the expression becomes hard to read.

## `match` / `case` (Python 3.10+)

Use `match` to compare one subject with literal patterns or alternatives:

```python
match command:
    case "start" | "resume":
        print("Starting")
    case "pause":
        print("Paused")
    case _:
        print("Unknown command")
```

`case _` is a wildcard and should normally come last. A bare name such as `case command` captures a value; it does not compare the subject to the variable named `command`. Use `if` for ranges and general Boolean conditions.

More detail: [Week 2 worked examples](../Month_1/Week_2/03_Examples.md), [nested conditions](../Month_1/Week_2/05_Examples.md), [conditional expressions](../Month_1/Week_2/06_Examples.md), and [`match` / `case`](../Month_1/Week_2/07_Examples.md).

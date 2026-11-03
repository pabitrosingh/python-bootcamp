# Week 2 / Example 2 - Boolean logic

Use `and` when all requirements must hold, `or` when either one is sufficient, and `not` to reverse a Boolean value.

```python
has_ticket = True
has_id = False

can_enter = has_ticket and has_id
print(can_enter)  # False

is_weekend = True
is_holiday = False
day_off = is_weekend or is_holiday
print(day_off)  # True

account_locked = False
print(not account_locked)  # True
```

Combine comparisons to express a range:

```python
score = 84
passed = score >= 60 and score <= 100
print(f"Valid passing score: {passed}")
```

Python also supports chained comparisons: `60 <= score <= 100`.

## Values used as conditions

Conditions do not have to be written as comparisons. Python treats `False`, `None`, numeric zero, and empty strings or collections as false; most other values are true.

```python
name = ""

if name:
    print(f"Hello, {name}")
else:
    print("A name has not been entered.")
```

An empty string is false, but the non-empty string `"False"` is true. When asking a yes/no question, compare the response explicitly:

```python
answer = input("Continue? (yes/no): ").strip().lower()
if answer == "yes":
    print("Continuing.")
```

## Short-circuit evaluation

For `and`, Python stops as soon as the left side is false. For `or`, it stops as soon as the left side is true. This lets the first condition guard an operation that is only safe when that condition holds:

```python
denominator = 0

if denominator != 0 and 10 / denominator > 1:
    print("The quotient is greater than one.")
else:
    print("The division condition was not met.")
```

Because `denominator != 0` is false, Python does not evaluate `10 / denominator`; no division-by-zero error occurs.
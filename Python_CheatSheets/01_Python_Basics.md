# Python Basics Cheat Sheet

Quick reference for the values, input, operators, and strings introduced in [Month 1, Week 1](../Month_1/Week_1/Topics.md).

## Run a script

```bash
python hello.py
```

## Output, variables, and types

```python
print("Hello, Python!")

name = "Asha"       # str: text
age = 20            # int: whole number
price = 12.50       # float: decimal number
is_ready = True     # bool: True or False

print(type(name))   # <class 'str'>
```

Names are case-sensitive. Use descriptive names such as `weekly_study_hours`.

## Input and conversion

`input()` always returns a string. Convert numeric text before doing arithmetic:

```python
name = input("Name: ").strip()
age = int(input("Age in years: "))
price = float(input("Price: "))

print(f"{name} is {age} years old.")
print(f"Price: ${price:.2f}")
```

`int("hello")` and `float("hello")` raise `ValueError`. See the [Week 4 error-handling sheet](./04_Functions_and_Errors.md) for safe input patterns.

## Arithmetic operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | Add | `2 + 3` → `5` |
| `-` | Subtract | `7 - 4` → `3` |
| `*` | Multiply | `3 * 4` → `12` |
| `/` | Divide (result is a float) | `7 / 2` → `3.5` |
| `//` | Floor division | `7 // 2` → `3` |
| `%` | Remainder | `7 % 2` → `1` |
| `**` | Power | `2 ** 3` → `8` |

Use parentheses to make the intended order clear:

```python
total = (2 + 3) * 4
```

## Strings

```python
first = "Ada"
last = "Lovelace"
full_name = first + " " + last
cheer = "Go! " * 3
message = f"Hello, {full_name}!"
```

Useful string methods:

```python
answer = input("Continue? ").strip().lower()
```

## Common reminders

- `=` assigns a value; `==` compares values.
- `input()` does not automatically turn digits into a number.
- Use f-strings to put values into readable text: `f"Age: {age}"`.
- Format decimal places with an f-string format specifier: `f"{price:.2f}"`.

Continue with the [Month 1 cheat sheet index](./README.md).

# Week 3 / Example 3 - `break`, `continue`, and filtering

`continue` skips the rest of the current pass. `break` exits the loop.

```python
for number in range(1, 8):
    if number == 3:
        continue
    if number == 6:
        break
    print(number)
```

The output is `1`, `2`, `4`, `5`: 3 is skipped, and the loop stops before printing 6.

Often a condition inside the loop is clearer than `continue`:

```python
total = 0
for number in range(1, 6):
    if number % 2 == 0:
        total = total + number

print(f"Sum of even values: {total}")
```

This prints 6. Practice tracing each loop one pass at a time.

String methods can check individual characters:

```python
password = "Python123"
has_uppercase = False
has_lowercase = False
has_digit = False

for character in password:
    if character.isupper():
        has_uppercase = True
    if character.islower():
        has_lowercase = True
    if character.isdigit():
        has_digit = True

print(has_uppercase, has_lowercase, has_digit)
```

Each flag starts as `False` and becomes `True` if the loop finds a matching character.
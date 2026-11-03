# Functions and Errors Cheat Sheet

Quick reference for [Month 1, Week 4: functions and input errors](../Month_1/Week_4/Week_4_Topics.md).

## Define and call a function

```python
def greet(name):
    print(f"Hello, {name}!")


greet("Asha")
```

- A **parameter** is a named input in the definition (`name`).
- An **argument** is the value passed in the call (`"Asha"`).
- A function body is indented.
- Defining a function does not run it; call it to execute it.

## Return a value

```python
def calculate_average(first_score, second_score):
    return (first_score + second_score) / 2


average = calculate_average(80, 90)
print(average)
```

`return` ends the function and sends a value back to its caller. Returning a calculation makes it reusable; printing displays text and does not replace a returned result.

## Scope

Variables assigned inside a function are normally local to that function:

```python
def calculate_total(price, quantity):
    total = price * quantity
    return total
```

Pass required values as parameters and return results rather than relying on global variables.

## Handle expected conversion errors

Converting invalid numeric text with `int()` or `float()` raises `ValueError`:

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("Enter a whole number.")
else:
    print(f"Next year: {age + 1}")
```

For retry behavior, catch the expected error and continue the loop:

```python
while True:
    score_text = input("Score (0-100): ")
    try:
        score = float(score_text)
    except ValueError:
        print("Enter a number.")
        continue

    if 0 <= score <= 100:
        break
    print("Score must be from 0 to 100.")
```

Catch a specific expected exception such as `ValueError`; a broad `except` can hide unrelated bugs.

## Design reminders

- Give a function one clear job and a descriptive name.
- Pass in the values it needs.
- Return calculated results; keep display code separate when practical.
- Validate user input at the point where it enters the program.

More: [Week 4 examples](../Month_1/Week_4/Week_4_Topics.md).

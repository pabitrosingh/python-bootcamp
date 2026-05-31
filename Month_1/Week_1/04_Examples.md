# Month 1 / Week 1: Day 4 — Control Flow (If, Elif, Else Statements)

Today we are covering how to make our Python programs make smart decisions using conditional logic and comparison operators.

---

## 1. Comparison Operators
Before Python can make a decision, it needs to compare values. Comparison expressions always result in a Boolean value (`True` or `False`).

* `==` Equal to
* `!=` Not equal to
* `>` Greater than
* `<` Less than
* `>=` Greater than or equal to
* `<=` Less than or equal to

```python
x = 10
y = 20

print(x < y)   # Output: True
print(x == y)  # Output: False
```

## 2. Basic if and else Structure
Python uses indentation (4 spaces or a tab) to define blocks of code that should only run when a condition is met.

```python
age = 19

if age >= 18:
    print("You are an adult!")
    print("You are allowed to vote.")
else:
    print("You are a minor.")
```

## 3. Handling Multiple Conditions with elif
If you have more than two possible outcomes, use elif (short for "else if"). Python will check conditions sequentially from top to bottom and run only the first block that is true.

```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # This will run!
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

## 4. Logical Operators (and, or, not)
You can combine multiple comparisons together to create complex rules.

- `and`: Returns `True` if both conditions are true.
- `or`: Returns `True` if at least one condition is true.
- `not`: Inverts the result (turns `True` to `False` and vice versa).

```python
has_ticket = True
has_id = False

# Using 'and' (Both must be True)
if has_ticket and has_id:
    print("Welcome to the concert!")
else:
    print("Access denied. You need both a ticket and your ID.")

# Using 'or' (At least one must be True)
if has_ticket or has_id:
    print("You have at least one valid item.")
```

## 4. Why did Python skip the traditional switch case?
Python’s design philosophy prioritizes readability and simplicity ("There should be one—and preferably only one—obvious way to do it"). The creators felt that a traditional switch statement didn't add any new capabilities because if-elif-else does the exact same job while keeping the language clean.

#### The Modern Python Way: match-case
If you are using a recent version of Python, you can use the new match-case syntax. It acts exactly like a switch case.

Here is how it looks compared to the if-elif-else structure we used:

```python
status_code = 404

match status_code:
    case 200:
        print("Success!")
    case 404:
        print("Not Found!")  # This will run!
    case 500:
        print("Server Error!")
    case _:
        print("Unknown Status Code")  # The underscore '_' acts like the 'default' case
```

#### Why use match-case over if-elif-else?
Cleanliness: It is much easier to read when you are checking a single variable against a long list of specific values.

The Wildcard (case _): The underscore acts as a catch-all safety net (like else or default) if none of the other conditions match.

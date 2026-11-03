# Week 4 / Example 4 - Handle invalid numeric input

Converting arbitrary text with `int()` can raise `ValueError`. Catch that expected error and explain how to try again.

```python
try:
    age = int(input("Age in whole years: "))
except ValueError:
    print("Please enter a whole number, such as 18.")
else:
    print(f"Next year you will be {age + 1}.")
```

For an interactive program, put the conversion in a loop so the user can correct a mistake:

```python
def ask_for_score():
    while True:
        score_text = input("Score from 0 to 100: ")
        try:
            score = float(score_text)
        except ValueError:
            print("Enter a number, such as 82 or 82.5.")
            continue

        if 0 <= score <= 100:
            return score
        print("The score must be between 0 and 100.")


print(f"Accepted score: {ask_for_score():.1f}")
```

Catch the specific expected exception (`ValueError`) rather than hiding unrelated programming errors with a broad `except`.
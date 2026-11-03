# Week 2 / Example 7 - `match`/`case`

Python 3.10 and newer has a `match` statement. It compares one subject value with patterns and runs the suite for the first matching case.

```python
command = "deposit"

match command:
    case "balance":
        print("Show the current balance.")
    case "deposit":
        print("Ask for a deposit amount.")
    case "withdraw":
        print("Ask for a withdrawal amount.")
    case _:
        print("Unknown command.")
```

`case _` is a wildcard that matches any value, so put it last. If no case matches and there is no wildcard, no branch runs. `match` does not fall through to later cases after a match.

## Match more than one literal

Use `|` between alternatives that should run the same branch:

```python
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case _:
        print("Not a recognized day")
```

## When to use it

- Use `match` when one value is being compared to a set of known patterns or alternatives.
- Use `if`/`elif` for ranges, arbitrary Boolean conditions, or decisions involving several independent values.
- A `match` case is a pattern, not an ordinary expression: `case command` would bind a name and match any value rather than compare against the variable. Use a literal such as `case "deposit"` for exact text.

Pattern matching can also destructure sequences and objects. Those patterns are beyond this beginner module; see the official [Python tutorial on `match`](https://docs.python.org/3/tutorial/controlflow.html#match-statements) and the [language reference](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement) for the full grammar and behavior.

# Week 2 - Decisions and Boolean logic

## Learning objectives

By the end of this week, you should be able to compare values, combine conditions, and select which code runs with `if`, `elif`, and `else`.

## Seven-day plan

1. Arithmetic, assignment, and operator precedence
2. Comparison operators and Boolean results; simple `if` and `else`
3. `if`/`elif`/`else` ladders and ordered choices
4. Nested decisions and Boolean logic with `and`, `or`, and `not`
5. Conditional expressions and `match`/`case` (Python 3.10+)
6. Complete the [exercises](./Exercises/) and [quiz](./Quiz/Quiz.md)
7. Build the [ATM Simulator](./Project/README.md)

## Worked examples

- [Example 1: arithmetic and comparisons](./01_Examples.md)
- [Example 2: Boolean logic](./02_Examples.md)
- [Example 3: `if`/`elif`/`else` ladder](./03_Examples.md)
- [Example 4: a transaction decision](./04_Examples.md)
- [Example 5: nested conditions](./05_Nested_Conditionals.md)
- [Example 6: conditional expressions](./06_Conditional_Expressions.md)
- [Example 7: `match`/`case`](./07_Match_Case.md)

## Common mistakes to check

- Use `==` to compare; a single `=` assigns a value.
- Put the most specific or highest threshold first in an `if`/`elif` chain.
- Use `and` when every condition must be true; use `or` when at least one must be true.
- Use nesting only when an inner decision depends on an outer decision; prefer a simple `elif` ladder for alternatives.
- Use a conditional expression for a short value choice, not for multi-step actions.
- Use `match` when comparing one subject to patterns; use `if` for general Boolean conditions and ranges.
- Indent the body of each branch consistently.

## Official references

- [Python tutorial: `if` statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Python tutorial: `match` statements](https://docs.python.org/3/tutorial/controlflow.html#match-statements)
- [Language reference: compound statements](https://docs.python.org/3/reference/compound_stmts.html)
- [Language reference: conditional expressions](https://docs.python.org/3/reference/expressions.html#conditional-expressions)
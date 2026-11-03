# Week 2 / Example 4 - Decide whether to approve a withdrawal

This single-transaction example uses input, numeric conversion, comparisons, and branches. It does not repeat the menu; loops are covered next week.

```python
balance = 100.00
amount = float(input("Withdrawal amount: "))

if amount <= 0:
    print("Enter an amount greater than zero.")
elif amount > balance:
    print("Insufficient funds.")
else:
    balance = balance - amount
    print(f"Withdrawal approved. New balance: ${balance:.2f}")
```

Test the three branches with `0`, `150`, and `25`. What happens if the user enters text instead of a number? That input error will be handled in Week 4.

For more complex dependent decisions, study [nested conditions](./05_Nested_Conditionals.md). For choosing a short value or a command branch, compare [conditional expressions](./06_Conditional_Expressions.md) and [`match`/`case`](./07_Match_Case.md).
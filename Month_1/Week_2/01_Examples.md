# Week 2 / Example 1 - Arithmetic and comparisons

Python follows ordinary arithmetic precedence: parentheses first, then exponentiation, multiplication/division, and addition/subtraction.

```python
price = 12.50
quantity = 3
subtotal = price * quantity
print(f"Subtotal: ${subtotal:.2f}")

print(2 + 3 * 4)      # 14
print((2 + 3) * 4)    # 20
```

Comparison operators return `True` or `False`:

| Operator | Meaning | Example |
|---|---|---|
| `==` | equal to | `score == 100` |
| `!=` | not equal to | `choice != "quit"` |
| `<` | less than | `age < 18` |
| `<=` | less than or equal to | `price <= budget` |
| `>` | greater than | `temperature > 25` |
| `>=` | greater than or equal to | `score >= 60` |

```python
balance = 40
withdrawal = 25

print(balance >= withdrawal)  # True
print(balance == 0)           # False
```

Try changing `withdrawal` to `50`. Predict both results before running the code. Remember that `=` assigns a value, while `==` compares two values.
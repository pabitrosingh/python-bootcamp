# Week 2 / Example 5 - Nested conditional statements

A nested conditional places one `if` statement inside another. Use it when the second decision only makes sense after the first condition is satisfied.

This example applies a delivery discount only to orders at or above the threshold, then checks whether the customer is a member:

```python
order_total = 60.00
is_member = True

if order_total >= 50:
    if is_member:
        discount_rate = 0.10
    else:
        discount_rate = 0.05
else:
    discount_rate = 0.0

discount = order_total * discount_rate
final_total = order_total - discount
print(f"Discount: ${discount:.2f}")
print(f"Final total: ${final_total:.2f}")
```

The inner membership decision only runs when the order reaches `$50`. Try all four combinations: below/at least `$50`, and member/non-member.

## Avoid unnecessary nesting

When choices are alternatives at the same level, an `if`/`elif` ladder is usually easier to scan:

```python
if order_total < 50:
    discount_rate = 0.0
elif is_member:
    discount_rate = 0.10
else:
    discount_rate = 0.05
```

Use the nested version when it makes the dependency between conditions clearer; use the ladder when it makes the alternatives clearer. Keep indentation consistent so each `else` visibly belongs to its `if`.

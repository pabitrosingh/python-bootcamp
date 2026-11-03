# Exercise 4 - Shipping decision

Ask for an order total and whether the customer is a member. Apply these rules:

- Orders below `$25` have a `$5` shipping fee.
- Orders of `$25` or more have free shipping.
- Members receive free shipping on any order.

Use a nested `if` to express the membership check inside the below-threshold order branch. Display the shipping fee and final total to two decimal places.

**Test:** Try a member and non-member with totals below `$25`, exactly `$25`, and above `$25`.

**Reflection:** Rewrite your decision as an `if`/`elif` ladder. Which structure makes the dependency easier to see?

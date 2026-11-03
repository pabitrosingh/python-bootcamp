# Week 2 quiz - answer key

1. `14`; use `(2 + 3) * 4` to get `20`.
2. `bool` (`True` or `False`).
3. `=` assigns; `==` compares.
4. `and` is true only when both sides are true. `or` is true when at least one side is true.
5. `True`.
6. A score of 95 also meets `score >= 80`; testing the highest band first prevents the broader branch from matching early.
7. `Insufficient`.
8. `10 <= temperature <= 25` (or `temperature >= 10 and temperature <= 25`).
9. Only the first true branch runs; later conditions are not tested.
10. Nest an `if` when a later choice depends on the earlier branch. Use `elif` when the options are alternatives at the same level.
11. `result = "pass" if score >= 60 else "retry"`.
12. No case suite runs; execution continues after the `match` statement.
13. It is a wildcard pattern that matches any subject not matched by an earlier case, so it is commonly used as a default branch.
14. `""` is false because it is empty; `"False"` is true because it is a non-empty string.
15. `and` short-circuits: when `denominator != 0` is false, Python does not evaluate the division on the right.

# Week 2 / Example 2 - Set operations

Set operations express comparisons between groups:

```python
morning = {"Ari", "Bo", "Cam"}
afternoon = {"Bo", "Dee"}

print(morning | afternoon)  # union: everyone in either group
print(morning & afternoon)  # intersection: in both groups
print(morning - afternoon)  # difference: morning only
print(morning ^ afternoon)  # symmetric difference: in exactly one
```

The matching methods are `union()`, `intersection()`, `difference()`, and `symmetric_difference()`. Each operation produces a new set.

**Try it:** Model two course rosters and find who takes both courses and who takes only one.
# Week 1 / Example 1 - Create, index, and update a list

A list stores an ordered sequence. Lists can contain repeated values and can be changed after they are created.

```python
tasks = ["read", "practice", "review"]
print(tasks[0])   # read
print(tasks[-1])  # review
print(len(tasks)) # 3

tasks[1] = "write code"
tasks.append("review")
print(tasks)
```

Indexes start at `0`; negative indexes count from the end. Accessing `tasks[3]` here raises `IndexError`, because the last valid index is `2`.

**Try it:** Add an item at the beginning with `insert(0, item)`. Then remove it with `pop(0)` and print the value returned by `pop()`.
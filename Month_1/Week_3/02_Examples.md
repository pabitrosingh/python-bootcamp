# Week 3 / Example 2 - `while` and a running total

Use `while` when repetition should continue until a condition changes.

```python
total = 0
count = 1

while count <= 4:
    total = total + count
    count = count + 1

print(f"Total: {total}")
```

The loop stops because `count` increases on every pass and eventually becomes 5. If the update is removed, the condition remains true and the loop does not stop.

An interactive sentinel loop ends when the user enters a chosen value:

```python
answer = ""
while answer != "quit":
    answer = input("Type 'quit' to finish: ").strip().lower()
print("Finished.")
```
# Loops Cheat Sheet

Quick reference for [Month 1, Week 3: repetition with loops](../Month_1/Week_3/Week_3_Topics.md).

## `for` loop

Use `for` to process each item in a sequence or repeat a known number of times:

```python
for character in "Python":
    print(character)

for number in range(1, 6):
    print(number)  # 1 through 5; stop is not included
```

`range(start, stop, step)` customizes the start and increment:

```python
for even_number in range(2, 11, 2):
    print(even_number)
```

## `while` loop

Use `while` when repetition continues while a condition is true:

```python
count = 1
while count <= 3:
    print(count)
    count = count + 1
```

Check that every pass can eventually make the condition false. Otherwise the loop may never stop.

## Loop control

```python
for number in range(1, 8):
    if number == 3:
        continue  # skip the rest of this pass
    if number == 6:
        break     # exit the loop
    print(number)
```

- `continue` moves to the next iteration.
- `break` exits the nearest enclosing loop.

## Accumulate a total

```python
total = 0
for number in range(1, 5):
    total = total + number
print(total)  # 10
```

## Common loop patterns

- Choose `for` when iterating through a sequence or known range.
- Choose `while` when a condition or sentinel value controls when to stop.
- Update loop state so a `while` condition can eventually become false.
- Trace nested loops one pass at a time; the inner loop completes for every outer iteration.

See the [Week 3 examples and exercises](../Month_1/Week_3/Week_3_Topics.md).

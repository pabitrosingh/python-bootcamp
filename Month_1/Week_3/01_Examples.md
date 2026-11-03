# Week 3 / Example 1 - `for` and `range`

Use a `for` loop when you want to process each item in a sequence or repeat a known number of times.

```python
for letter in "Python":
    print(letter)
```

`range(stop)` starts at zero and stops before `stop`:

```python
for number in range(1, 6):
    print(number)
```

This prints 1 through 5. The end value is not included. `range(start, stop, step)` lets you select a starting value and step:

```python
for even_number in range(2, 11, 2):
    print(even_number)
```

Try changing the start, stop, and step values.
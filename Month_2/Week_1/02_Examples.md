# Week 1 / Example 2 - Slices and list methods

A slice selects items from a list. The stop position is excluded, and an omitted boundary uses the start or end of the list.

```python
scores = [72, 85, 91, 68, 100]
print(scores[1:4])  # [85, 91, 68]
print(scores[:2])   # [72, 85]
print(scores[::2])  # [72, 91, 100]
print(scores[::-1]) # a reversed copy
```

Common methods have different effects:

```python
scores.append(88)          # add one item
scores.extend([77, 80])    # add each item from an iterable
scores.insert(0, 60)       # insert before index 0
scores.remove(100)         # remove the first matching value
last_score = scores.pop()  # remove and return the last item
```

`remove(value)` raises `ValueError` if the value is absent. `pop(index)` raises `IndexError` if that index is invalid.

**Try it:** Make a list of five colors. Print the middle three with a slice, then append another color and display the list.
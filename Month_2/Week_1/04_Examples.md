# Week 1 / Example 4 - Comprehensions, sorting, and copies

A list comprehension builds a new list from an iterable:

```python
values = [1, 2, 3, 4, 5, 6]
squares = [value * value for value in values]
even_squares = [value * value for value in values if value % 2 == 0]
print(squares)       # [1, 4, 9, 16, 25, 36]
print(even_squares)  # [4, 16, 36]
```

Keep comprehensions to one clear transformation/filter. A regular `for` loop is easier to read when the logic has multiple steps.

```python
names = ["Mina", "alex", "Bo"]
print(sorted(names, key=str.casefold))  # new list
names.sort(key=str.casefold)            # changes names in place
```

Assignment aliases the same list; a shallow copy creates a different outer list:

```python
original = [10, 20]
alias = original
copy = original.copy()
alias.append(30)
print(original)  # [10, 20, 30]
print(copy)      # [10, 20]
```

**Try it:** Create a comprehension of the lengths of non-empty words in `["red", "", "blue"]`.
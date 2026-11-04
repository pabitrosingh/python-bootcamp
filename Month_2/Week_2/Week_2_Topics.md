# Week 2 - Sets and dictionaries

## Learning objectives

By the end of this week, you should be able to use sets for uniqueness and membership, use dictionaries for key-based lookup, safely read and update dictionary entries, and combine collections to model simple records.

## Seven-day plan

1. Create sets; understand uniqueness and membership
2. Set union, intersection, difference, and symmetric difference
3. Create dictionaries, access keys, and use `get()`
4. Add, update, remove, and iterate over dictionary entries
5. Use nested collections and choose a suitable structure
6. Complete the [exercises](./Exercises/) and [quiz](./Quiz/Quiz.md)
7. Build the [Contact Manager](./Project/README.md)

## Core ideas

- A set stores unique hashable values and does not provide positional indexing. Use `set()` for an empty set; `{}` creates an empty dictionary.
- `in` checks set membership. Set operations include `|` (union), `&` (intersection), `-` (difference), and `^` (symmetric difference).
- A dictionary maps unique, hashable keys to values. Keys are not accessed by position.
- `record[key]` raises `KeyError` when the key is absent; `record.get(key, default)` provides a fallback without changing the dictionary.
- Use `items()` to iterate over key-value pairs. Do not rely on a dictionary being a sorted mapping; explicitly sort keys when ordered output is required.
- A shallow copy duplicates only the outer collection. Nested mutable values remain shared.

## Worked examples

- [Example 1: set uniqueness and membership](./01_Examples.md)
- [Example 2: set operations](./02_Examples.md)
- [Example 3: dictionary lookup and update](./03_Examples.md)
- [Example 4: nested records and safe access](./04_Examples.md)

## Project

Build a [Contact Manager](./Project/README.md) backed by a dictionary. It demonstrates add, search, update, delete, input validation, and sorted display.

## Official references

- [Tutorial: Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Tutorial: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Tutorial: Looping Techniques](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques)
- [Language Reference: Set displays](https://docs.python.org/3/reference/expressions.html#set-displays)
- [Language Reference: Dictionary displays](https://docs.python.org/3/reference/expressions.html#dict)

## Checklist

- [ ] I can choose a set to remove duplicate values and check membership.
- [ ] I can use `get()` when a key may not exist.
- [ ] I can explain how a list of dictionaries differs from one dictionary.
- [ ] I can update a record without accidentally changing it when validation fails.
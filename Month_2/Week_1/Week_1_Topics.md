# Week 1 - Lists and tuples

## Learning objectives

By the end of this week, you should be able to create and update lists, use indexing and slicing, iterate without modifying a collection unexpectedly, use a comprehension for a simple transformation, and explain when a tuple is a better fit.

## Seven-day plan

1. List literals, indexing, negative indexes, and `len()`
2. Slicing and common list methods
3. Iterating over and searching a list
4. List comprehensions and copying versus aliasing
5. Tuples, unpacking, and immutable records
6. Complete the [exercises](./Exercises/) and [quiz](./Quiz/Quiz.md)
7. Review the [worked examples](./01_Examples.md) through [Example 5](./05_Examples.md)

## Core ideas

- Lists are ordered and mutable. An index starts at zero; an invalid index raises `IndexError`.
- A slice `items[start:stop:step]` selects a range and excludes `stop`. Slices produce a new list.
- `append()` adds one item, `extend()` adds items from an iterable, `insert()` adds at an index, and `remove()`/`pop()` delete items in different ways.
- `items.sort()` changes a list in place and returns `None`; `sorted(items)` returns a new sorted list.
- Assignment such as `second = first` creates another reference to the same list. Use `first.copy()` or `first[:]` for a shallow copy.
- Tuples are ordered and immutable. They are useful for fixed records and unpacking; a tuple can contain mutable objects, but its slots cannot be reassigned.
- Use a comprehension for a clear, compact transformation or filter; use a regular loop when it reads more clearly or has side effects.

## Worked examples

- [Example 1: create, index, and update a list](./01_Examples.md)
- [Example 2: slice and use list methods](./02_Examples.md)
- [Example 3: iterate, search, and build results](./03_Examples.md)
- [Example 4: comprehensions and copying](./04_Examples.md)
- [Example 5: tuples and unpacking](./05_Examples.md)

## Official references

- [Tutorial: More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Tutorial: Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Tutorial: List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Language Reference: Subscriptions and Slicings](https://docs.python.org/3/reference/expressions.html#subscriptions)
- [Language Reference: List displays](https://docs.python.org/3/reference/expressions.html#lists)

## Checklist

- [ ] I can predict the result of a slice without running it.
- [ ] I can distinguish a mutation from a function that returns a new list.
- [ ] I can explain why two names may refer to the same mutable list.
- [ ] I can unpack a tuple into named variables.
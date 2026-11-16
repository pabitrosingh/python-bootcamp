# Exercise 2 - Create an iterator

Implement `RangeByStep(start, stop, step)` as an iterable that yields values from `start` up to but not including `stop`, advancing by `step`.

Requirements:

- Support positive and negative steps.
- Reject a zero step with `ValueError`.
- Each call to `iter(range_by_step)` should produce a fresh iterator.
- Verify that the result matches the built-in `range` for positive, negative, and empty ranges.

Hint: Separate the reusable iterable from its iterator state, or delegate to `range`.

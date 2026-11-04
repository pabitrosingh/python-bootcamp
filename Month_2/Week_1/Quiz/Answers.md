# Week 1 quiz answers - Lists and tuples

1. The first element is at index `0`; `-1` selects the last element.
2. `[20, 30]`. The start is included and the stop index is excluded.
3. `append()` adds its argument as one item; `extend()` adds each item from the iterable.
4. `numbers.sort()` changes the list in place and returns `None`; `sorted(numbers)` returns a new sorted list.
5. Both names refer to the same list, so the appended item is visible through `original`.
6. `("tea",)`; the comma makes it a tuple.
7. No. The tuple's references cannot be reassigned, but the contained list can still be mutated.
8. `[number * number for number in range(4)]`

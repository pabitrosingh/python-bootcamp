# Week 1 / Example 3 - A custom iterator

An iterator stores its current position and produces one value at a time:

```python
class Countdown:
    def __init__(self, start):
        self._next_value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_value <= 0:
            raise StopIteration
        value = self._next_value
        self._next_value -= 1
        return value


for number in Countdown(3):
    print(number)
```

The `for` loop obtains an iterator, repeatedly calls `next()`, and finishes when `StopIteration` is raised. Because `Countdown` is itself an iterator, it is single-use: iterating over the same instance again does not restart the count.

**Try it:** Change the class so that `iter(countdown)` creates an independent iterator instead of making the iterable and iterator the same object.
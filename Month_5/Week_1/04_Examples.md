# Week 1 / Example 4 - A generator pipeline

Generator functions provide the iterator protocol without manually maintaining `__next__` state:

```python
def nonblank_lines(lines):
    for line in lines:
        cleaned = line.strip()
        if cleaned:
            yield cleaned


def words(lines):
    for line in lines:
        yield from line.split()


source = ["  red apple  ", "", "green pear"]
for word in words(nonblank_lines(source)):
    print(word)
```

`yield` suspends the function until the next value is requested. `yield from` delegates iteration to another iterable. The pipeline only processes data as the outer loop asks for it.

**Try it:** Add a generator that filters out words shorter than five characters without building an intermediate list.
# Week 1 Quiz - Answer key

1. It is equivalent to rebinding the function as `task = decorate(task)`.
2. It copies metadata such as the original function's name and docstring to the wrapper, and exposes the wrapped function through `__wrapped__`.
3. `StopIteration`.
4. An iterable can provide an iterator, usually through `__iter__()`. An iterator implements `__next__()` and is also an iterable that returns itself from `__iter__()`.
5. The call creates a generator object; the function body begins when the generator is advanced, for example by `next()` or a `for` loop.
6. It produces no further values. Create a new generator to iterate again.
7. A generator can process a large input without retaining all results at once. A list is better when values must be reused, indexed, or inspected repeatedly.
8. No. `yield from` delegates iteration to the supplied iterable.

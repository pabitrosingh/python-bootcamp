# Week 1 / Example 1 - A function decorator

A decorator can add behavior before and after a function call without changing the function's body:

```python
from functools import wraps
from time import perf_counter


def report_duration(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        started = perf_counter()
        try:
            return function(*args, **kwargs)
        finally:
            elapsed = perf_counter() - started
            print(f"{function.__name__} took {elapsed:.6f} seconds")

    return wrapper


@report_duration
def total(values):
    return sum(values)


print(total([1, 2, 3]))
```

`@report_duration` is shorthand for `total = report_duration(total)`. `wraps` copies useful metadata from the original function to `wrapper`. The `finally` block reports duration whether the wrapped call returns or raises; it does not catch or suppress exceptions.

**Try it:** Add a keyword-only option to enable or disable the report.
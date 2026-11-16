# Week 2 / Example 3 - Futures and worker exceptions

Use `submit()` when each task needs different arguments or when results should be handled as they complete:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed


def reciprocal(value):
    return 1 / value


with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(reciprocal, value) for value in (2, 0, 4)]
    for future in as_completed(futures):
        try:
            print(future.result())
        except ZeroDivisionError as error:
            print(f"task failed: {error}")
```

`submit()` returns a `Future`. Calling `result()` returns the worker's value or raises the exception produced by that worker. Handle only errors the application can meaningfully recover from; do not silently discard failed work.

**Try it:** Keep a mapping from each `Future` to its original input so a failure report identifies the task.
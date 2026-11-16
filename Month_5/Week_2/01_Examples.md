# Week 2 / Example 1 - Concurrent I/O with threads

Threads are useful when tasks spend much of their time waiting. This example simulates waiting without making network requests:

```python
from concurrent.futures import ThreadPoolExecutor
from time import sleep


def check_item(item):
    sleep(0.1)  # Simulate waiting for I/O
    return f"{item}: complete"


items = ["alpha", "beta", "gamma"]
with ThreadPoolExecutor(max_workers=3) as executor:
    for result in executor.map(check_item, items):
        print(result)
```

`map` yields results in input order even if tasks finish in a different order. A pool limits the number of active worker threads.

**Try it:** Change the number of workers and compare elapsed time with a sequential loop. Explain why this simulated delay is not a benchmark of CPU work.
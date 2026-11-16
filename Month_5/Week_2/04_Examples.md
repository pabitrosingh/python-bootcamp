# Week 2 / Example 4 - Sharing state safely

Prefer collecting independent return values to having worker threads mutate the same list or dictionary. If threads must coordinate, use synchronization primitives:

```python
from concurrent.futures import ThreadPoolExecutor
from threading import Lock


total = 0
lock = Lock()


def add(value):
    global total
    with lock:
        total += value


with ThreadPoolExecutor(max_workers=4) as executor:
    list(executor.map(add, range(1_001)))

print(total)
```

The lock protects the read-modify-write operation. For this simple reduction, a clearer design is to have each task return a partial result and combine those results in the caller, avoiding shared state altogether.

**Try it:** Rewrite the example so each worker returns a value and the main thread computes the total.
# Week 3 / Example 2 - Concurrent tasks with `gather`

Awaiting each coroutine in sequence waits for one to finish before starting the next. `gather` allows independent coroutines to make progress concurrently:

```python
import asyncio


async def fetch_label(label, delay):
    await asyncio.sleep(delay)
    return f"{label} ready"


async def main():
    results = await asyncio.gather(
        fetch_label("first", 0.2),
        fetch_label("second", 0.1),
    )
    print(results)


asyncio.run(main())
```

Results remain in the order of the awaitables passed to `gather`, not their completion order. These sleeps simulate asynchronous waiting and do not contact a service.

**Try it:** Add a third task and verify result ordering.
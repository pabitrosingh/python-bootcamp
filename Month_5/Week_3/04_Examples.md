# Week 3 / Example 4 - Offload blocking I/O

A blocking function called directly from a coroutine stalls the event loop. `asyncio.to_thread()` can run a blocking I/O function in a worker thread:

```python
import asyncio
from time import sleep


def blocking_read(label):
    sleep(0.2)  # Stand in for a blocking file or network operation
    return f"{label} read"


async def main():
    results = await asyncio.gather(
        asyncio.to_thread(blocking_read, "first"),
        asyncio.to_thread(blocking_read, "second"),
    )
    print(results)


asyncio.run(main())
```

This is suitable for some blocking I/O, not CPU-heavy pure-Python work. If the operation has an asynchronous API, prefer awaiting that API rather than wrapping it in a thread.

**Try it:** Compare the example with calling `blocking_read` directly inside `main`. Explain why one blocks other coroutines.
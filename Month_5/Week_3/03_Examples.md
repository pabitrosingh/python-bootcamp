# Week 3 / Example 3 - Timeouts and cancellation

Use a timeout when an operation must not wait forever:

```python
import asyncio


async def slow_operation():
    try:
        await asyncio.sleep(5)
        return "finished"
    finally:
        print("cleanup runs")


async def main():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=0.1)
    except TimeoutError:
        print("operation timed out")
    else:
        print(result)


asyncio.run(main())
```

When the timeout expires, cancellation is sent to the coroutine. The `finally` suite runs as the coroutine unwinds. Cleanup code should not swallow cancellation unless there is a specific, documented reason.

**Try it:** Add a `finally` block in `main` that records when timeout handling has completed.
# Week 3 / Example 1 - Run a coroutine

`asyncio.run()` creates an event loop for a top-level async program:

```python
import asyncio


async def greet(name):
    await asyncio.sleep(0.1)
    return f"Hello, {name}"


async def main():
    message = await greet("Ada")
    print(message)


if __name__ == "__main__":
    asyncio.run(main())
```

`greet("Ada")` creates a coroutine object. `await` inside `main` lets the event loop drive that coroutine until it returns.

**Try it:** Remove the `await` from `main` and observe that the coroutine is not executed as intended.
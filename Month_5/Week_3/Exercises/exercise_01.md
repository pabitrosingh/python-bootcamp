# Exercise 1 - Concurrent coroutine tasks

Write an async function that simulates loading a named item with `asyncio.sleep()` and returns a result. In `main()`, load several independent items with `asyncio.gather()`.

Requirements:

- Run the top-level coroutine with `asyncio.run()`.
- Show that gathered results correspond to the input order.
- Compare with a sequential `await` loop.
- Do not use blocking `time.sleep()` inside a coroutine.

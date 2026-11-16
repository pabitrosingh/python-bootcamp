# Exercise 2 - Time limit and cleanup

Write a coroutine that awaits a long sleep inside `try/finally`. Use `asyncio.wait_for()` with a short timeout.

Requirements:

- Catch the timeout at the caller.
- Verify that the coroutine's cleanup runs after cancellation.
- Do not catch and silently suppress `asyncio.CancelledError`.
- Explain how a timeout differs from successfully completing the operation.

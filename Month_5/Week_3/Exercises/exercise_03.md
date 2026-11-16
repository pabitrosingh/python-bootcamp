# Exercise 3 - Move blocking I/O off the event loop

Create a synchronous function that simulates a blocking read with `time.sleep()`. Call two instances using `asyncio.to_thread()` and `asyncio.gather()`.

Requirements:

- Keep the blocking function synchronous.
- Return and print both results.
- Compare with calling the function directly inside an `async def`.
- Explain why `to_thread()` is suited to blocking I/O but is not a general speed-up for CPU-bound Python code.

# Week 3 - Asynchronous programming

## Learning objectives

By the end of this week, you should be able to define and run coroutines, use `await` and `asyncio.gather`, coordinate concurrent tasks, propagate cancellation, and identify blocking calls that would stall an event loop.

## Seven-day plan

1. Understand coroutines, the event loop, and cooperative scheduling
2. Define `async def` functions and run a coroutine with `asyncio.run`
3. Await non-blocking operations and start concurrent tasks
4. Handle task results, errors, timeouts, and cancellation
5. Compare `asyncio` with threads and processes
6. Complete the [exercises](./Exercises/) and [quiz](./Quiz/Quiz.md)
7. Review the examples and describe one asynchronous I/O workflow

## Core ideas

- Calling an `async def` function creates a coroutine object; it does not by itself run the coroutine to completion.
- `await` suspends the current coroutine until an awaitable completes, allowing the event loop to run other tasks.
- `asyncio.run()` is the usual top-level entry point for a standalone async program; do not call it from an already-running event loop.
- `asyncio.gather()` runs awaitables concurrently and collects results in the order supplied.
- Async code is cooperative: a task yields at `await`. A long CPU loop or blocking function can prevent every other task on that event loop from progressing.
- Use `asyncio.to_thread()` to offload a blocking I/O function when appropriate; use processes for CPU-heavy Python work.
- Timeouts and cancellation are part of normal async control flow. Use `try/finally` or async context managers for cleanup.

## Worked examples

- [Example 1: run a coroutine](./01_Examples.md)
- [Example 2: concurrent tasks with `gather`](./02_Examples.md)
- [Example 3: timeouts and cancellation](./03_Examples.md)
- [Example 4: offload blocking I/O](./04_Examples.md)

## Official references

- [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html)
- [Developing with `asyncio`](https://docs.python.org/3/library/asyncio-dev.html)
- [Language Reference: Coroutines](https://docs.python.org/3/reference/compound_stmts.html#coroutines)
- [Language Reference: The `await` expression](https://docs.python.org/3/reference/expressions.html#await-expression)

## Checklist

- [ ] I can distinguish a coroutine function from a coroutine object.
- [ ] I can explain why `await asyncio.sleep(...)` yields but `time.sleep(...)` blocks.
- [ ] I can run independent coroutines concurrently and collect results.
- [ ] I can explain how a timeout or cancellation affects cleanup.
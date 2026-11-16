# Exercise 3 - Handle future failures

Use `ThreadPoolExecutor.submit()` to schedule several tasks, one of which raises a predictable exception.

Requirements:

- Keep a mapping from each `Future` to its input.
- Iterate with `as_completed()`.
- Call `future.result()` so worker exceptions are surfaced.
- Report the failed input and exception without hiding unrelated failures.

Extension: Add a timeout to `future.result()` and explain what a timeout does and does not cancel.

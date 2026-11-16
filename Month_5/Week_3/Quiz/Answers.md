# Week 3 Quiz - Answer key

1. A coroutine object; it must be awaited or scheduled to run.
2. It suspends the current coroutine so the event loop can run other ready tasks.
3. It manages an event loop and runs the supplied awaitable to completion; it is normally used once at the top level of a standalone async program.
4. It blocks the event-loop thread, preventing other tasks on that loop from making progress.
5. In the order of the awaitables supplied, not completion order.
6. It cancels the awaited operation and raises a timeout exception to the caller; cancellation cleanup may still need to run.
7. It does not yield control, so other tasks on the event loop cannot run until that work finishes.
8. To offload a blocking I/O function so the event loop can continue running other tasks.

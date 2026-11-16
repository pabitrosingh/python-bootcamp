# Exercise 1 - Compare sequential and threaded I/O

Write a function that simulates a blocking I/O operation with `time.sleep()` and returns a label. Run the same set of labels sequentially and with `ThreadPoolExecutor`.

Requirements:

- Return results in the input order.
- Use a context manager for the executor.
- Compare results for equality before comparing elapsed times.
- Explain why the artificial sleep models waiting, not CPU-bound computation.

Keep the workload small enough to run quickly and do not treat a single timing as a general performance guarantee.

# Week 2 - Threads, processes, and executors

## Learning objectives

By the end of this week, you should be able to identify I/O-bound and CPU-bound work, submit work to thread and process pools, collect results and exceptions, and recognize shared-state and process-startup concerns.

## Seven-day plan

1. Distinguish concurrency, parallelism, and sequential execution
2. Learn when threads help with I/O-bound work and how shared state creates races
3. Use `ThreadPoolExecutor` and `Future` to run bounded concurrent tasks
4. Use `ProcessPoolExecutor` for CPU-heavy work and protect the entry point
5. Measure a small sequential and concurrent workload and explain overhead
6. Complete the [exercises](./Exercises/) and [quiz](./Quiz/Quiz.md)
7. Review the examples and select a concurrency strategy for a given workload

## Core ideas

- Concurrency lets multiple tasks make progress; parallelism means tasks execute at the same instant on separate compute resources.
- Threads share a process's memory and are often useful for I/O-bound tasks. Protect shared mutable state or avoid sharing it.
- In standard GIL-enabled CPython builds, threads usually do not speed up CPU-bound pure-Python work. Python implementations and free-threaded builds can differ.
- Processes have separate memory and can execute Python code on multiple cores, but task arguments and results must be transferable and process creation has overhead.
- `concurrent.futures` provides one high-level interface for threads and processes. A `Future` represents a result that may not be ready yet.
- Always use a context manager for an executor when practical; retrieve results so worker exceptions are surfaced.
- Multiprocessing programs need an import-safe entry point guarded by `if __name__ == "__main__":`.

## Worked examples

- [Example 1: concurrent I/O with threads](./01_Examples.md)
- [Example 2: CPU work with processes](./02_Examples.md)
- [Example 3: futures and exceptions](./03_Examples.md)
- [Example 4: sharing state safely](./04_Examples.md)

## Project

Build the [Directory Monitoring Tool](./Project/README.md), which snapshots file metadata and reports added, modified, and removed files.

## Official references

- [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html)
- [`threading`](https://docs.python.org/3/library/threading.html)
- [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html)
- [Tutorial: Multi-threading](https://docs.python.org/3/tutorial/stdlib2.html#multi-threading)
- [Language Reference: The `with` statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)

## Checklist

- [ ] I can explain when thread or process pools might help.
- [ ] I can collect results from futures and identify where worker exceptions appear.
- [ ] I can explain why a process pool needs importable, picklable callables and arguments.
- [ ] I can explain why shared mutable state needs coordination.
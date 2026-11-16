# Week 2 Quiz - Answer key

1. Concurrency is overlapping progress on multiple tasks; parallelism is simultaneous execution, typically on separate cores or compute resources.
2. A thread pool is often a reasonable start for blocking I/O because threads can wait concurrently without separate process startup and memory costs.
3. Separate processes have separate interpreters and can run Python code on multiple cores, avoiding the usual single-interpreter GIL limitation.
4. It raises the exception produced by the worker when the result is retrieved.
5. A child process must be able to import or otherwise resolve the callable, and a module-level function is generally easier to serialize and import.
6. On spawn-based platforms, child processes import the module. Without the guard, top-level launch code could run again in each child.
7. Updates can interleave and produce a race condition or inconsistent result unless access is coordinated.
8. Pool startup, task scheduling, data transfer, synchronization, or result collection adds overhead.

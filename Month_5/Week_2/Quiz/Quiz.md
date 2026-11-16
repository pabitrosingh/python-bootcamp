# Week 2 Quiz - Threads, processes, and executors

1. What is the difference between concurrency and parallelism?
2. Which is a reasonable starting choice for many blocking network requests: a thread pool or a process pool? Why?
3. Why might a process pool help CPU-bound pure-Python work in standard GIL-enabled CPython?
4. What does `Future.result()` do when the worker raised an exception?
5. Why should a process-pool worker function generally be defined at module scope?
6. Why is the `if __name__ == "__main__":` guard important for multiprocessing?
7. What problem can occur when multiple threads modify shared mutable state?
8. Name one reason a concurrent solution may be slower than a sequential one.

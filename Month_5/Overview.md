# Month 5 - Advanced Python

## Goal

Use Python's advanced language features and standard library to build efficient, maintainable programs that process data lazily, coordinate concurrent work, and automate repeatable tasks.

By the end of the month, you should be able to:

- Explain how decorators wrap and preserve the behavior of functions
- Build iterators and generators that produce values on demand
- Choose between sequential, threaded, process-based, and asynchronous execution
- Use `asyncio` for concurrent I/O without blocking the event loop
- Design small automation scripts with safe defaults, useful logs, and clear command-line options
- Build, run, and test a web scraper, file automation suite, and directory monitoring tool

## Prerequisites

Complete [Month 1](../Month_1/Overview.md), [Month 2](../Month_2/Overview.md), [Month 3](../Month_3/Overview.md), and [Month 4](../Month_4/Overview.md). You should be comfortable with functions, exceptions, collections, classes, files, tests, and basic command-line use. The projects use Python 3.10+ and the standard library only.

## Weekly plan

| Week | Focus | Project |
|---|---|---|
| [Week 1](./Week_1/Week_1_Topics.md) | Decorators, iterators, and generators | [Web Scraper](./Week_1/Project/README.md) |
| [Week 2](./Week_2/Week_2_Topics.md) | Threads, processes, and executors | [Monitoring Tool](./Week_2/Project/README.md) |
| [Week 3](./Week_3/Week_3_Topics.md) | Asynchronous programming with `asyncio` | Practice and review |
| [Week 4](./Week_4/Week_4_Topics.md) | Automation and integration | [Automation Suite](./Week_4/Project/README.md) |

Each week includes worked examples, exercises, a quiz, and an answer key. Weeks 1, 2, and 4 also include a project, following the Month 3 structure. Examples use synthetic/local data so they can be run without external services.

## Choosing a concurrency model

Concurrency is a way to make progress on multiple tasks during the same period; it does not always mean parallel execution on multiple CPU cores.

| Workload | Useful starting point | Reason |
|---|---|---|
| Blocking network or file I/O | `ThreadPoolExecutor` or `asyncio` | Tasks can progress while another operation waits |
| CPU-heavy pure-Python work | `ProcessPoolExecutor` | Separate processes can use multiple CPU cores |
| Sequential tasks or tiny workloads | Ordinary functions and loops | Concurrency overhead can exceed any benefit |

Measure representative workloads before choosing a design. Threads share memory and need synchronization when mutable state is shared. Processes have separate memory and require work/results to be transferable. Async code only yields control when it awaits; calling a blocking function in a coroutine still blocks the event loop.

## Run the projects and tests

The projects have no third-party dependencies. From the repository root, run:

```bash
python -m unittest -v \
    Month_5.Week_1.Project.test_scraper \
    Month_5.Week_2.Project.test_monitor \
    Month_5.Week_4.Project.test_organizer
```

The project READMEs document their command-line interfaces and safety defaults. The scraper makes network requests only when explicitly run with a URL; tests do not access the network. The file organizer previews changes by default and requires `--apply` to move files.

## Month-end completion checklist

- [ ] Complete the weekly exercises and quizzes without relying on the answer keys.
- [ ] Explain how a decorator receives and returns a callable, and why `functools.wraps` is useful.
- [ ] Explain the iterator protocol and why generators can process large inputs lazily.
- [ ] Choose threads, processes, or `asyncio` based on workload and constraints.
- [ ] Explain why multiprocessing entry points need an `if __name__ == "__main__":` guard.
- [ ] Run all three weekly projects and their tests; confirm the organizer previews rather than moves files by default.
- [ ] Describe one limitation and one possible extension for each project.

## Official references

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [The Python Language Reference](https://docs.python.org/3/reference/index.html)
- [Tutorial: Iterators](https://docs.python.org/3/tutorial/classes.html#iterators)
- [Tutorial: Generators](https://docs.python.org/3/tutorial/classes.html#generators)
- [Language Reference: Function definitions](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
- [Language Reference: The `yield` statement](https://docs.python.org/3/reference/simple_stmts.html#the-yield-statement)
- [`functools`](https://docs.python.org/3/library/functools.html)
- [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html)
- [`threading`](https://docs.python.org/3/library/threading.html)
- [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html)
- [`asyncio`](https://docs.python.org/3/library/asyncio.html)
- [`pathlib`](https://docs.python.org/3/library/pathlib.html)
- [`argparse`](https://docs.python.org/3/library/argparse.html)
- [`logging`](https://docs.python.org/3/library/logging.html)
- [`html.parser`](https://docs.python.org/3/library/html.parser.html)
- [`urllib.request`](https://docs.python.org/3/library/urllib.request.html)
- [`time.monotonic`](https://docs.python.org/3/library/time.html#time.monotonic)
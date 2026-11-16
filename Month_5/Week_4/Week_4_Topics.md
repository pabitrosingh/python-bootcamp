# Week 4 - Automation and project integration

## Learning objectives

By the end of this week, you should be able to build a repeatable command-line task, work with filesystem paths portably, log useful events, make a safe dry-run workflow, and combine Month 5 concepts in small automation projects.

## Seven-day plan

1. Design a small automation task with explicit inputs and outputs
2. Use `pathlib` for directory traversal and file operations
3. Use `argparse` for command-line arguments and `logging` for diagnostics
4. Practice previews, bounded work, validation, and error reporting
5. Build or extend the [Automation Suite](./Project/README.md)
6. Run its tests and review the [Web Scraper](../Week_1/Project/README.md) and [Monitoring Tool](../Week_2/Project/README.md)
7. Run the tests and complete the [exercises](./Exercises/) and [quiz](./Quiz/Quiz.md)

## Core ideas

- Automation should be repeatable, have explicit inputs, validate assumptions, and report failures.
- Prefer `pathlib.Path` over hand-built path strings; test filesystem changes in temporary directories.
- Make potentially destructive operations preview-only by default and require an explicit flag to apply them.
- Use `argparse` to define a clear CLI and `logging` for diagnostics; reserve printed output for user-facing results.
- Use `time.monotonic()` for measuring elapsed time or scheduling intervals because wall-clock time can change.
- A web scraper should use bounded timeouts, identify itself appropriately, parse HTML rather than assume tags are well-formed, and follow the target site's terms and access policies.
- A polling monitor has a detection delay determined by its polling interval and is not a substitute for OS-level event notification.

## Worked examples

- [Example 1: organize paths with `pathlib`](./01_Examples.md)
- [Example 2: a safe command-line interface](./02_Examples.md)
- [Example 3: log an automation task](./03_Examples.md)
- [Example 4: measure elapsed time](./04_Examples.md)

## Project

Build the [Automation Suite](./Project/README.md), a file organizer that previews its proposed moves and requires an explicit `--apply` flag before changing files.

## Official references

- [`pathlib`](https://docs.python.org/3/library/pathlib.html)
- [`argparse`](https://docs.python.org/3/library/argparse.html)
- [`logging`](https://docs.python.org/3/library/logging.html)
- [`time.monotonic`](https://docs.python.org/3/library/time.html#time.monotonic)
- [`html.parser`](https://docs.python.org/3/library/html.parser.html)
- [`urllib.request`](https://docs.python.org/3/library/urllib.request.html)
- [The Python Tutorial: Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

## Checklist

- [ ] I can make an automation command preview changes before applying them.
- [ ] I can distinguish user-facing output from diagnostic logs.
- [ ] I can explain why monotonic time is preferred for elapsed-time measurement.
- [ ] I can describe the limitations of a polling-based monitor and a simple HTML parser.
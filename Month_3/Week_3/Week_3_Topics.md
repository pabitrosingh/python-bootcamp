# Week 3 - Exceptions, logging, and the standard library

## Learning objectives

By the end of this week, you should be able to distinguish syntax errors from runtime exceptions, catch only failures you can handle, define a meaningful custom exception, add context when re-raising, use hierarchical logging, and select standard-library modules for common needs.

## Seven-day plan

1. Read tracebacks and distinguish syntax errors from exceptions
2. Catch specific exceptions and use `else` and `finally`
3. Define domain exceptions and chain lower-level failures
4. Use loggers, levels, and structured context
5. Work with `datetime`, `pathlib`, `enum`, and `collections`
6. Complete the [exercises](./Exercises/) and [quiz](./Quiz/Quiz.md)
7. Review project error handling and testing

## Core ideas

- Catch an exception at the layer that can respond meaningfully. Let unexpected failures propagate.
- Prefer a narrow `except` clause. `except Exception` can hide programming errors if used as a fallback.
- Raise `ValueError` for a valid type with an invalid value; use a custom exception when callers need to distinguish a domain failure.
- Use `raise NewError(...) from error` to preserve the original cause while adding domain context.
- `finally` runs during normal and exceptional control flow; use context managers for resources that need reliable cleanup.
- Libraries should use `logging.getLogger(__name__)` and should not configure the application's root logger.
- `datetime`, `pathlib`, `enum`, `collections`, `decimal`, and `json` provide reusable standard-library tools. Prefer them to custom substitutes when they fit the problem.

## Worked examples

- [Example 1: catch a specific exception](./01_Examples.md)
- [Example 2: custom exceptions and chaining](./02_Examples.md)
- [Example 3: logging levels and module loggers](./03_Examples.md)
- [Example 4: useful standard-library modules](./04_Examples.md)

## Official references

- [Tutorial: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Language Reference: The `try` statement](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement)
- [Built-in exceptions](https://docs.python.org/3/library/exceptions.html)
- [The `logging` module](https://docs.python.org/3/library/logging.html)
- [The `datetime` module](https://docs.python.org/3/library/datetime.html)
- [The `pathlib` module](https://docs.python.org/3/library/pathlib.html)
- [The `enum` module](https://docs.python.org/3/library/enum.html)
- [The `collections` module](https://docs.python.org/3/library/collections.html)

## Checklist

- [ ] I can explain the cause shown at the end of a traceback.
- [ ] I catch only exceptions I can meaningfully handle.
- [ ] I can preserve the original cause when translating an exception.
- [ ] I use a module logger and avoid configuring logging inside reusable code.

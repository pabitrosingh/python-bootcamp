# Week 3 quiz answers - Exceptions, logging, and the standard library

1. A syntax error prevents code from being parsed; an exception occurs during execution.
2. Broad handlers can hide unrelated bugs and make failures look like successful results.
3. The original exception as the new exception's cause, preserving diagnostic context.
4. Only when the `try` suite completes without raising an exception.
5. The application entry point configures logging; a reusable library should use a named logger and leave configuration to its caller.
6. `WARNING`.
7. `datetime` (use a timezone such as `timezone.utc` for an aware datetime).
8. `pathlib` for filesystem paths and `enum` for named constants with a constrained set of values.

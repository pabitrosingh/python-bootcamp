# Week 4 - Design patterns and integration

## Learning objectives

By the end of this week, you should be able to recognize a design pattern's intent, implement a small Strategy or Factory, keep storage behind a Repository-style boundary, and integrate object-oriented code with exceptions, logging, standard-library types, and tests.

## Seven-day plan

1. Recognize patterns as named solutions, not mandatory templates
2. Implement Strategy with interchangeable behavior
3. Use a simple Factory to select a concrete object
4. Use a Repository boundary to isolate persistence
5. Combine domain models, validation, logging, and tests
6. Complete the [exercises](./Exercises/) and [quiz](./Quiz/Quiz.md)
7. Build the [Employee Management System](./Project/README.md)

## Core ideas

- Patterns describe recurring design tradeoffs. Prefer the smallest design that solves the current problem.
- Strategy encapsulates interchangeable behavior behind a consistent interface.
- A Factory centralizes object creation when callers should not know construction details.
- A Repository separates domain behavior from storage details. A dictionary-backed repository is enough for an in-memory project; a database is out of scope until Month 4.
- Dependency injection means passing a collaborator into an object instead of constructing a concrete dependency internally.
- Test patterns through observable behavior; tests should not depend on private implementation details.

## Worked examples

- [Example 1: choose a pattern for its intent](./01_Examples.md)
- [Example 2: Strategy](./02_Examples.md)
- [Example 3: Factory and Repository](./03_Examples.md)
- [Example 4: integrate and test a service](./04_Examples.md)

## Project

Build the [Employee Management System](./Project/README.md), using Strategy objects for compensation calculations and a simple manager for employee records.

## Official references

- [Tutorial: Classes](https://docs.python.org/3/tutorial/classes.html)
- [The `abc` module](https://docs.python.org/3/library/abc.html)
- [The `typing` module](https://docs.python.org/3/library/typing.html)
- [The `unittest.mock` module](https://docs.python.org/3/library/unittest.mock.html)
- [The `logging` module](https://docs.python.org/3/library/logging.html)

## Checklist

- [ ] I can explain the problem that each pattern in this week solves.
- [ ] I can replace a concrete collaborator with a test double.
- [ ] I can describe why an in-memory repository is not durable storage.
- [ ] I have completed and tested the Employee Management System.

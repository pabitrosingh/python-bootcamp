# Week 2 - SOLID and testing

## Learning objectives

By the end of this week, you should be able to describe SOLID as a set of design heuristics, separate responsibilities, inject dependencies for testability, and write behavior-focused unit tests with `unittest` and pytest.

## Seven-day plan

1. Single Responsibility and Open/Closed principles
2. Liskov Substitution and Interface Segregation principles
3. Dependency Inversion and dependency injection
4. Arrange-Act-Assert and isolated unit tests
5. `unittest` fixtures, assertions, and test discovery
6. pytest functions, assertions, parametrization, and test discovery
7. Complete the [exercises](./Exercises/) and [quiz](./Quiz/Quiz.md), then build the [Inventory Management System](./Project/README.md)

## Core ideas

- SOLID is a collection of design guidelines, not a checklist that requires one class per method.
- Single Responsibility: keep a module or class focused on a cohesive reason to change.
- Open/Closed: make likely extensions possible without repeatedly editing stable core logic.
- Liskov Substitution: a subtype should preserve the behavior callers expect from its base type.
- Interface Segregation: prefer small role-specific interfaces over broad ones clients do not need.
- Dependency Inversion: high-level policy should not be tightly coupled to low-level details. Pass collaborators into the code that uses them.
- A unit test checks observable behavior for a focused unit. Tests should be deterministic and should not rely on external services or real user input.
- `unittest` is in the standard library. pytest is a separate package; its plain functions and `assert` statements make concise tests. pytest can also run `unittest` test cases.

## Worked examples

- [Example 1: separate responsibilities](./01_Examples.md)
- [Example 2: substitute implementations safely](./02_Examples.md)
- [Example 3: a focused `unittest` test](./03_Examples.md)
- [Example 4: pytest-style tests](./04_Examples.md)

## Project

Build the [Inventory Management System](./Project/README.md). Its service receives a product repository so its business rules can be tested independently of storage.

## Official references

- [The Python Tutorial: Classes](https://docs.python.org/3/tutorial/classes.html)
- [The `unittest` module](https://docs.python.org/3/library/unittest.html)
- [unittest command-line interface](https://docs.python.org/3/library/unittest.html#command-line-interface)
- [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html)

## Checklist

- [ ] I can describe one practical example for each SOLID principle.
- [ ] I can test a class without invoking its command-line interface or external services.
- [ ] I can run standard-library tests with `python -m unittest`.
- [ ] I can write pytest tests and understand that pytest is installed separately.

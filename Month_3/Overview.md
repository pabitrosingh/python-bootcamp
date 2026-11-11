# Month 3 - Professional Python

## Goal

Use classes and composition to model a problem, apply SOLID ideas to keep code changeable, test behavior, handle and report failures, and recognize when a design pattern or standard-library tool makes a solution clearer.

By the end of the month, you should be able to:

- Define classes with clear responsibilities and protect valid object state
- Prefer composition where it avoids unnecessary inheritance
- Explain and apply the SOLID principles at a practical level
- Write focused unit tests with `unittest` and understand pytest-style tests
- Raise specific exceptions and preserve useful error context
- Use the `logging` module instead of printing diagnostic messages
- Choose useful standard-library modules for common application tasks
- Recognize Strategy, Factory, and Repository patterns without forcing them into every program
- Build and test the [Banking Application](./Week_1/Project/README.md), [Inventory Management System](./Week_2/Project/README.md), and [Employee Management System](./Week_4/Project/README.md)

## Prerequisites

Complete [Month 1](../Month_1/Overview.md) and [Month 2](../Month_2/Overview.md). You should be comfortable with functions, collections, modules, files, and basic exceptions. Python 3.10 or newer is recommended. Project implementations use only the standard library.

## Weekly plan

| Week | Focus | Project |
|---|---|---|
| [Week 1](./Week_1/Week_1_Topics.md) | Classes, instances, encapsulation, inheritance, composition, and data classes | [Banking Application](./Week_1/Project/README.md) |
| [Week 2](./Week_2/Week_2_Topics.md) | SOLID principles, unit testing, and pytest | [Inventory Management System](./Week_2/Project/README.md) |
| [Week 3](./Week_3/Week_3_Topics.md) | Exceptions, logging, and useful standard-library modules | Practice and review |
| [Week 4](./Week_4/Week_4_Topics.md) | Design patterns and integration | [Employee Management System](./Week_4/Project/README.md) |

Each week has worked examples, exercises, a quiz, and an answer key. Try them before reading the answers. The applications are runnable from the repository root and include tests.

## Testing tools

The projects use Python's built-in `unittest`, so no packages are needed to run their tests. pytest is an optional third-party test runner; it can also discover and run `unittest` tests. Install it with `python -m pip install pytest` if you want to run the pytest examples or use its additional features.

From the repository root, run all Month 3 project tests with:

```bash
python -m unittest -v Month_3.Week_1.Project.test_banking \
    Month_3.Week_2.Project.test_inventory \
    Month_3.Week_4.Project.test_employee_management
```

Or, after installing pytest:

```bash
python -m pytest Month_3
```

## Month-end completion checklist

- [ ] Complete the weekly exercises and quizzes without relying on the answer keys.
- [ ] Build and test all three roadmap projects.
- [ ] Explain which SOLID principles helped you make a change safely.
- [ ] Explain the difference between raising, handling, and logging an exception.
- [ ] Identify the Strategy, Factory, and Repository ideas in the examples.
- [ ] Run the tests from the repository root and confirm they pass.

## Official references

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [The Python Language Reference](https://docs.python.org/3/reference/index.html)
- [Classes in the Python Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [Errors and Exceptions in the Python Tutorial](https://docs.python.org/3/tutorial/errors.html)
- [The `unittest` module](https://docs.python.org/3/library/unittest.html)
- [The `logging` module](https://docs.python.org/3/library/logging.html)
- [The `dataclasses` module](https://docs.python.org/3/library/dataclasses.html)
- [The `datetime` module](https://docs.python.org/3/library/datetime.html)
- [The `decimal` module](https://docs.python.org/3/library/decimal.html)
- [The `enum` module](https://docs.python.org/3/library/enum.html)
- [The `pathlib` module](https://docs.python.org/3/library/pathlib.html)
- [pytest documentation](https://docs.pytest.org/)

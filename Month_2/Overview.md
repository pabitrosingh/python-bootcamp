# Month 2 - Python Data Structures

## Goal

Learn to choose and combine Python's built-in data structures, persist simple data in files, organize code into modules and packages, and solve a small problem recursively.

By the end of the month, you should be able to:

- Choose between lists, tuples, sets, and dictionaries for a task
- Safely update, search, sort, and transform collections
- Read and write text and JSON files with context managers
- Import code from modules and packages without running a script's command-line interface accidentally
- Explain a recursive function's base case and recursive step
- Build and test the [Contact Manager](./Week_2/Project/README.md), [File Analyzer](./Week_3/Project/README.md), and [Library Management System](./Week_4/Project/README.md)

## Prerequisites

Complete [Month 1](../Month_1/Overview.md), especially variables, loops, functions, and basic error handling. Python 3.10 or newer is recommended. The examples use only the standard library.

## Weekly plan

| Week | Focus | Project |
|---|---|---|
| [Week 1](./Week_1/Week_1_Topics.md) | Lists, indexing, slicing, iteration, comprehensions, and tuples | Collection practice |
| [Week 2](./Week_2/Week_2_Topics.md) | Sets, dictionaries, nested data, and choosing a collection | [Contact Manager](./Week_2/Project/README.md) |
| [Week 3](./Week_3/Week_3_Topics.md) | Text and JSON files, exceptions, modules, and packages | [File Analyzer](./Week_3/Project/README.md) |
| [Week 4](./Week_4/Week_4_Topics.md) | Recursion, tracing, safe base cases, and integration | [Library Management System](./Week_4/Project/README.md) |

Each week includes worked examples, exercises, a quiz, and an answer key. Try the exercises and quiz before reading their answers. Run examples yourself and change the input values to check your understanding.

## Data-structure selection guide

| Need | Start with |
|---|---|
| Ordered, changeable sequence; duplicates are allowed | `list` |
| Ordered, fixed record; duplicates may be meaningful | `tuple` |
| Unique values and membership checks | `set` |
| Look up a value by a meaningful key | `dict` |

These are starting points, not rigid rules. A program often combines structures, such as a list of dictionaries.

## Month-end completion checklist

- [ ] Complete the weekly exercises and quizzes without relying on the answer key.
- [ ] Build and run all three roadmap projects.
- [ ] Run each project's automated tests with `python -m unittest -v`.
- [ ] Explain which data structure each project uses and why.
- [ ] Explain the base case and progress measure of a recursive function.

## Official references

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) is a practical introduction.
- [The Python Language Reference](https://docs.python.org/3/reference/index.html) specifies Python syntax and semantics.

Each weekly guide links to the relevant chapters. The tutorial is the recommended starting point; the reference is useful when you want precise rules.
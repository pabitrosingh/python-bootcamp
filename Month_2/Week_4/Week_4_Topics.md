# Week 4 - Recursion and integration

## Learning objectives

By the end of this week, you should be able to identify a recursive function's base case and recursive step, trace a small call sequence, explain why progress toward a base case matters, and combine collections and file operations in a tested program.

## Seven-day plan

1. Trace function calls and identify the stopping condition
2. Write a recursive function with a base case
3. Recursively process a sequence or nested structure
4. Compare recursion with an iterative solution
5. Review input validation and test edge cases
6. Complete the [exercises](./Exercises/) and [quiz](./Quiz/Quiz.md)
7. Build the [Library Management System](./Project/README.md)

## Core ideas

- A recursive function calls itself on a smaller or simpler problem.
- A base case returns without making another recursive call.
- Each recursive step must make measurable progress toward the base case. Without progress, recursion does not terminate and eventually raises `RecursionError`.
- Python does not optimize tail calls. Prefer iteration for straightforward repetition or unbounded input sizes.
- Recursion is useful when the data or problem is naturally nested, such as a tree. For a list of flat records, a loop is usually simpler.
- Use tests for empty input, the smallest valid input, typical input, and invalid input where applicable.

## Worked examples

- [Example 1: countdown and base cases](./01_Examples.md)
- [Example 2: sum a sequence recursively](./02_Examples.md)
- [Example 3: reverse a string recursively](./03_Examples.md)
- [Example 4: recursion versus iteration](./04_Examples.md)

## Project

Build the [Library Management System](./Project/README.md), an integrated application using a dictionary of books, validation, JSON persistence, and unit tests. Recursion is practiced in the examples and exercises; it is not forced into the library's flat-record operations.

## Official references

- [Tutorial: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Tutorial: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Language Reference: Function definitions](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
- [Language Reference: Expressions and calls](https://docs.python.org/3/reference/expressions.html#calls)
- [Library Reference: Recursion limit](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit)

## Checklist

- [ ] I can point to the base case and recursive step in a function.
- [ ] I can show that each call receives a smaller problem.
- [ ] I can explain when an iterative solution is safer or clearer.
- [ ] I can test the library project without relying on a particular working directory.
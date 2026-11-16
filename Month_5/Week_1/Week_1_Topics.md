# Week 1 - Decorators, iterators, and generators

## Learning objectives

By the end of this week, you should be able to explain higher-order functions, write a decorator that accepts arguments, preserve wrapped function metadata, implement the iterator protocol, and use generators for lazy processing.

## Seven-day plan

1. Review functions as objects and functions that accept or return callables
2. Write a basic decorator and trace the wrapped function call
3. Preserve metadata with `functools.wraps` and build a decorator factory
4. Explore `iter()` and `next()` and the iterator protocol
5. Write generator functions, generator expressions, and a lazy pipeline
6. Complete the [exercises](./Exercises/) and [quiz](./Quiz/Quiz.md)
7. Review the examples and sketch a streaming data-processing task

## Core ideas

- A decorator takes a callable and returns a callable; `@decorate` is equivalent to rebinding a function through `decorate(function)`.
- A wrapper should normally use `functools.wraps` so the wrapped function's name, documentation, and annotations remain available.
- A decorator factory accepts configuration and returns the actual decorator.
- An iterable can provide an iterator. An iterator returns itself from `__iter__()` and produces values through `__next__()` until `StopIteration`.
- A generator function uses `yield`; each call returns a generator iterator whose state is resumed as values are requested.
- Laziness can reduce memory use, but a generator is generally one-pass and errors may occur only when it is consumed.

## Worked examples

- [Example 1: a function decorator](./01_Examples.md)
- [Example 2: a configurable retry decorator](./02_Examples.md)
- [Example 3: a custom iterator](./03_Examples.md)
- [Example 4: a generator pipeline](./04_Examples.md)
- [Example 5: generator expressions and exhaustion](./05_Examples.md)

## Project

Build the [Web Scraper](./Project/README.md), a single-page scraper that extracts titles, headings, and links while bounding network time and response size.

## Official references

- [Tutorial: More on Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
- [Tutorial: Iterators](https://docs.python.org/3/tutorial/classes.html#iterators)
- [Tutorial: Generators](https://docs.python.org/3/tutorial/classes.html#generators)
- [Tutorial: Generator Expressions](https://docs.python.org/3/tutorial/classes.html#generator-expressions)
- [Language Reference: Function definitions](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
- [Language Reference: The `yield` statement](https://docs.python.org/3/reference/simple_stmts.html#the-yield-statement)
- [`functools.wraps`](https://docs.python.org/3/library/functools.html#functools.wraps)

## Checklist

- [ ] I can explain the order in which a decorator and its wrapper run.
- [ ] I can preserve wrapped function metadata with `functools.wraps`.
- [ ] I can distinguish an iterable from an iterator.
- [ ] I can explain what happens when an iterator is exhausted.
- [ ] I can describe when lazy evaluation is helpful and when it is not.
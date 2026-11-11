# Week 1 - Object-oriented programming

## Learning objectives

By the end of this week, you should be able to define a class, create instances, distinguish instance data from class data, validate state through methods, choose composition or inheritance deliberately, and use `dataclass` for straightforward data records.

## Seven-day plan

1. Classes, instances, attributes, and methods
2. Instance state, class attributes, and `self`
3. Encapsulation, properties, and invariants
4. Inheritance, overriding, and `super()`
5. Composition and data classes
6. Complete the [exercises](./Exercises/) and [quiz](./Quiz/Quiz.md)
7. Build the [Banking Application](./Project/README.md)

## Core ideas

- A class defines behavior and the shape of its instances; creating a class does not create an instance.
- `self` refers to the instance receiving a method call. It is an ordinary parameter name by convention.
- Instance attributes belong to each object. Class attributes are shared through the class unless shadowed on an instance.
- Keep invariants valid by validating values at the boundary where state changes. A leading underscore signals an implementation detail; it does not make an attribute inaccessible.
- Inheritance models a genuine “is a” relationship. Composition (“has a”) is often simpler when an object can delegate work to another object.
- A `@dataclass` is useful for data-centric classes; it can generate methods such as `__init__` and `__repr__`. It does not automatically validate annotations or make instances immutable.

## Worked examples

- [Example 1: define a class and create instances](./01_Examples.md)
- [Example 2: instance and class attributes](./02_Examples.md)
- [Example 3: protect object invariants](./03_Examples.md)
- [Example 4: inheritance and composition](./04_Examples.md)
- [Example 5: data classes](./05_Examples.md)

## Official references

- [Tutorial: A First Look at Classes](https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes)
- [Tutorial: Class and Instance Variables](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)
- [Tutorial: Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Tutorial: Private Variables](https://docs.python.org/3/tutorial/classes.html#private-variables)
- [Language Reference: Class definitions](https://docs.python.org/3/reference/compound_stmts.html#class-definitions)
- [Library Reference: `dataclasses`](https://docs.python.org/3/library/dataclasses.html)

## Checklist

- [ ] I can explain what `self` refers to in an instance method.
- [ ] I can explain why a mutable class attribute can be shared unexpectedly.
- [ ] I can state the invariant a class is responsible for preserving.
- [ ] I can choose composition instead of inheritance when it fits better.

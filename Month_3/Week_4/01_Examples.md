# Week 4 / Example 1 - Choose patterns for their intent

Patterns are vocabulary for common designs, not requirements to add more classes:

| Need | Possible pattern |
|---|---|
| Swap a behavior without changing its caller | Strategy |
| Centralize selection or construction of an object | Factory |
| Keep domain logic independent of storage | Repository |

If a function with one `if` statement already solves the problem clearly, a hierarchy of factories and strategies may be unnecessary. Add a pattern when there are real variants or a boundary that benefits from isolation.

**Try it:** Pick a program you have written. Identify one concrete source of likely change and decide whether a pattern would make that change simpler.

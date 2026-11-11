# Week 2 quiz answers - SOLID and testing

1. Keep a module or class focused around a cohesive responsibility and reason to change.
2. No. It means make likely extensions possible without repeatedly changing stable code; changes are still sometimes necessary.
3. The behavioral promises of the base type; callers should not be surprised by the subtype.
4. Small interfaces prevent clients from depending on operations they do not need or cannot support.
5. Supplying a dependency to the code that uses it rather than constructing that dependency internally.
6. External state makes tests slower, less deterministic, and harder to isolate. Use a fake or mock for the boundary.
7. `python -m unittest` (or `python -m unittest discover`).
8. No. pytest is a third-party package. Yes, pytest can collect and run `unittest.TestCase` tests.

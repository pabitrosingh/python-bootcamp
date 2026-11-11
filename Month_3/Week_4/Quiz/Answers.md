# Week 4 quiz answers - Design patterns and integration

1. It packages interchangeable behavior behind a common operation so a caller can use different algorithms without changing its own logic.
2. It centralizes the selection or construction of an object, keeping those details out of its callers.
3. It separates domain code from storage details through a small set of data operations.
4. It provides deterministic, fast storage behavior without requiring external infrastructure.
5. No. Its data exists only in process memory.
6. The code receives the collaborator from outside and can be given a fake or in-memory implementation for tests.
7. When the pattern adds more indirection than it removes or there is no real variation or boundary to solve.
8. Examples include supplying a new Strategy, adding a Factory-supported implementation, or implementing a new Repository behind the same interface.

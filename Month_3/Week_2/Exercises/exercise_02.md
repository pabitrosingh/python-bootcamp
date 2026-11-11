# Exercise 2 - Test a service through a dependency

Write a small service that saves named notes through a repository collaborator. Pass the repository into the service constructor rather than creating it inside the service.

**Test:** Use a dictionary-backed fake repository to test saving and duplicate-name handling.

**Try next:** Define a small `Protocol` for the methods the service needs and annotate the constructor.

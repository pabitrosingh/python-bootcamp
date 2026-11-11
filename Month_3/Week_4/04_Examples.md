# Week 4 / Example 4 - Integrate and test a service

Keep the entry point small and test the service independently of the console:

```python
import logging

logger = logging.getLogger(__name__)


class EmployeeService:
    def __init__(self, repository):
        self.repository = repository

    def add(self, employee):
        self.repository.save(employee)
        logger.info("Employee added", extra={"employee_id": employee.employee_id})


class FakeRepository:
    def __init__(self):
        self.records = {}

    def save(self, employee):
        self.records[employee.employee_id] = employee
```

A unit test can pass `FakeRepository` to `EmployeeService`, call `add`, and assert that the employee is stored. The test does not need to configure logging or create a real database. Validate input at the service or domain boundary, raise a meaningful exception for invalid data, and let the application decide how to present the error.

**Try it:** Add a duplicate-identifier rule, define the expected exception, and test that a duplicate does not replace the first employee.

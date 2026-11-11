# Project - Employee Management System

Build an in-memory employee manager with interchangeable compensation strategies. The project integrates classes, validation, a Factory, the Strategy pattern, logging, standard-library types, and unit tests.

The reference implementation is [`employee_management.py`](./employee_management.py), with acceptance tests in [`test_employee_management.py`](./test_employee_management.py).

## Features

- Create employees with a unique ID, name, department, and compensation strategy
- Support fixed monthly salary and hourly wage calculations
- List employees in stable ID order, look up an employee, and remove one
- Calculate one employee's pay or a payroll mapping
- Reject duplicate/missing IDs, invalid employee data, and invalid compensation inputs
- Log management actions without configuring logging inside the reusable manager

## Run

From the repository root:

```bash
python -m Month_3.Week_4.Project.employee_management
python -m unittest -v Month_3.Week_4.Project.test_employee_management
```

For hourly employees, pass non-negative hours worked to `calculate_pay` or provide their hours in the payroll mapping. Salaried employees receive their configured monthly amount.

## Acceptance checklist

- [ ] The factory creates the appropriate pay strategy for each employment type.
- [ ] The manager rejects duplicate IDs and reports missing IDs with a domain exception.
- [ ] Payroll uses the selected strategy rather than type-specific logic in the manager.
- [ ] Invalid pay inputs leave employee records unchanged.
- [ ] Employee listing is deterministic.
- [ ] All tests pass.

## Extensions

- Add a commission strategy without adding an employment-type branch to `EmployeeManager`.
- Add an employee repository and inject it into the manager.
- Export a report to UTF-8 text with `pathlib`; keep file operations outside the employee model.

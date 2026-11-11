"""An in-memory employee manager using Strategy and Factory patterns."""

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from enum import Enum
import logging
from typing import Protocol


logger = logging.getLogger(__name__)


class EmployeeError(Exception):
    """Base class for expected employee-management errors."""


class InvalidEmployeeError(EmployeeError, ValueError):
    """Raised when employee or compensation data is invalid."""


class DuplicateEmployeeError(EmployeeError):
    """Raised when an employee ID is already in use."""


class EmployeeNotFoundError(EmployeeError, LookupError):
    """Raised when an employee ID is not present."""


class EmploymentType(Enum):
    SALARIED = "salaried"
    HOURLY = "hourly"


def _positive_money(value: Decimal | str | int) -> Decimal:
    try:
        amount = Decimal(str(value))
    except (InvalidOperation, ValueError) as error:
        raise InvalidEmployeeError("compensation must be a finite decimal") from error
    if not amount.is_finite() or amount <= 0:
        raise InvalidEmployeeError("compensation must be finite and positive")
    return amount


def _hours(value: Decimal | str | int | None) -> Decimal:
    if value is None:
        raise InvalidEmployeeError("hours worked are required for hourly pay")
    try:
        amount = Decimal(str(value))
    except (InvalidOperation, ValueError) as error:
        raise InvalidEmployeeError("hours worked must be a finite decimal") from error
    if not amount.is_finite() or amount < 0:
        raise InvalidEmployeeError("hours worked must be finite and non-negative")
    return amount


class PayStrategy(Protocol):
    def calculate_pay(
        self, hours_worked: Decimal | str | int | None = None
    ) -> Decimal: ...


@dataclass(frozen=True)
class SalariedPay:
    monthly_salary: Decimal

    def __post_init__(self) -> None:
        object.__setattr__(self, "monthly_salary", _positive_money(self.monthly_salary))

    def calculate_pay(
        self, hours_worked: Decimal | str | int | None = None
    ) -> Decimal:
        return self.monthly_salary


@dataclass(frozen=True)
class HourlyPay:
    hourly_rate: Decimal

    def __post_init__(self) -> None:
        object.__setattr__(self, "hourly_rate", _positive_money(self.hourly_rate))

    def calculate_pay(
        self, hours_worked: Decimal | str | int | None = None
    ) -> Decimal:
        return self.hourly_rate * _hours(hours_worked)


@dataclass(frozen=True)
class Employee:
    employee_id: str
    name: str
    department: str
    pay_strategy: PayStrategy

    def __post_init__(self) -> None:
        employee_id = self.employee_id.strip()
        name = self.name.strip()
        department = self.department.strip()
        if not employee_id or not name or not department:
            raise InvalidEmployeeError("employee ID, name, and department are required")
        object.__setattr__(self, "employee_id", employee_id)
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "department", department)
        if not callable(getattr(self.pay_strategy, "calculate_pay", None)):
            raise InvalidEmployeeError("pay strategy must provide calculate_pay")


def create_employee(
    employee_id: str,
    name: str,
    department: str,
    employment_type: EmploymentType | str,
    compensation: Decimal | str | int,
) -> Employee:
    """Factory that builds an employee with the selected pay strategy."""
    try:
        kind = EmploymentType(employment_type)
    except ValueError as error:
        raise InvalidEmployeeError(
            f"unsupported employment type: {employment_type!r}"
        ) from error

    if kind is EmploymentType.SALARIED:
        strategy: PayStrategy = SalariedPay(_positive_money(compensation))
    else:
        strategy = HourlyPay(_positive_money(compensation))
    return Employee(employee_id, name, department, strategy)


class EmployeeManager:
    """Manage employees and delegate pay calculations to their strategies."""

    def __init__(self) -> None:
        self._employees: dict[str, Employee] = {}

    def add_employee(self, employee: Employee) -> None:
        if employee.employee_id in self._employees:
            raise DuplicateEmployeeError(
                f"employee {employee.employee_id!r} already exists"
            )
        self._employees[employee.employee_id] = employee
        logger.info(
            "Employee added",
            extra={"employee_id": employee.employee_id},
        )

    def get_employee(self, employee_id: str) -> Employee:
        try:
            return self._employees[employee_id]
        except KeyError as error:
            raise EmployeeNotFoundError(
                f"employee {employee_id!r} was not found"
            ) from error

    def remove_employee(self, employee_id: str) -> Employee:
        employee = self.get_employee(employee_id)
        del self._employees[employee_id]
        logger.info("Employee removed", extra={"employee_id": employee_id})
        return employee

    def list_employees(self) -> list[Employee]:
        return sorted(
            self._employees.values(), key=lambda employee: employee.employee_id
        )

    def calculate_pay(
        self,
        employee_id: str,
        hours_worked: Decimal | str | int | None = None,
    ) -> Decimal:
        employee = self.get_employee(employee_id)
        return employee.pay_strategy.calculate_pay(hours_worked)

    def payroll(
        self,
        hours_by_employee: dict[str, Decimal | str | int] | None = None,
    ) -> dict[str, Decimal]:
        hours = hours_by_employee or {}
        return {
            employee.employee_id: employee.pay_strategy.calculate_pay(
                hours.get(employee.employee_id)
            )
            for employee in self.list_employees()
        }


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    manager = EmployeeManager()
    manager.add_employee(
        create_employee("E-101", "Ada Lovelace", "Engineering", "salaried", "7200")
    )
    manager.add_employee(
        create_employee("E-102", "Grace Hopper", "Engineering", "hourly", "85")
    )
    payroll = manager.payroll({"E-102": "40"})
    for employee_id, amount in payroll.items():
        print(f"{employee_id}: ${amount:.2f}")


if __name__ == "__main__":
    main()

import unittest
from decimal import Decimal

from Month_3.Week_4.Project.employee_management import (
    DuplicateEmployeeError,
    EmployeeManager,
    EmployeeNotFoundError,
    EmploymentType,
    HourlyPay,
    InvalidEmployeeError,
    SalariedPay,
    create_employee,
)


class EmployeeManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager = EmployeeManager()
        self.salaried = create_employee(
            " E-2 ", " Ada ", " Engineering ", EmploymentType.SALARIED, "7200"
        )
        self.hourly = create_employee("E-1", "Grace", "Operations", "hourly", "85")
        self.manager.add_employee(self.salaried)
        self.manager.add_employee(self.hourly)

    def test_factory_builds_expected_strategies(self):
        self.assertIsInstance(self.salaried.pay_strategy, SalariedPay)
        self.assertIsInstance(self.hourly.pay_strategy, HourlyPay)
        self.assertEqual(self.salaried.employee_id, "E-2")
        self.assertEqual(self.salaried.name, "Ada")

    def test_strategies_calculate_pay(self):
        self.assertEqual(self.manager.calculate_pay("E-2"), Decimal("7200"))
        self.assertEqual(self.manager.calculate_pay("E-1", "40"), Decimal("3400"))

    def test_hourly_pay_requires_valid_hours(self):
        for value in (None, "-1", "NaN", "not hours"):
            with self.subTest(value=value), self.assertRaises(InvalidEmployeeError):
                self.manager.calculate_pay("E-1", value)
        self.assertEqual(self.manager.calculate_pay("E-1", "0"), Decimal("0"))

    def test_payroll_is_sorted_and_uses_each_strategy(self):
        self.assertEqual(
            self.manager.payroll({"E-1": "10"}),
            {"E-1": Decimal("850"), "E-2": Decimal("7200")},
        )

    def test_duplicate_and_missing_employee_errors(self):
        with self.assertRaises(DuplicateEmployeeError):
            self.manager.add_employee(self.salaried)
        with self.assertRaises(EmployeeNotFoundError):
            self.manager.get_employee("missing")
        with self.assertRaises(EmployeeNotFoundError):
            self.manager.remove_employee("missing")

    def test_remove_returns_employee_and_updates_listing(self):
        removed = self.manager.remove_employee("E-1")
        self.assertIs(removed, self.hourly)
        self.assertEqual([employee.employee_id for employee in self.manager.list_employees()], ["E-2"])

    def test_factory_rejects_bad_type_or_compensation(self):
        with self.assertRaises(InvalidEmployeeError):
            create_employee("E-3", "Lin", "Research", "contractor", "50")
        with self.assertRaises(InvalidEmployeeError):
            create_employee("E-3", "Lin", "Research", "hourly", "NaN")

    def test_employee_requires_complete_identity(self):
        with self.assertRaises(InvalidEmployeeError):
            create_employee(" ", "Lin", "Research", "hourly", "50")


if __name__ == "__main__":
    unittest.main()

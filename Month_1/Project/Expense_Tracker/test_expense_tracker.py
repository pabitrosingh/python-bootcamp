import unittest

from expense_tracker import add_expense, calculate_total


class ExpenseTrackerTests(unittest.TestCase):
    def test_add_expense_strips_description_and_records_amount(self):
        expenses = []
        expense = add_expense(expenses, " Bus fare ", 2.5)
        self.assertEqual(expense, {"description": "Bus fare", "amount": 2.5})
        self.assertEqual(expenses, [expense])

    def test_add_expense_rejects_blank_description(self):
        expenses = []
        with self.assertRaisesRegex(ValueError, "Description cannot be blank"):
            add_expense(expenses, "  ", 2.5)
        self.assertEqual(expenses, [])

    def test_add_expense_rejects_non_positive_amount(self):
        for amount in (0, -1):
            with self.subTest(amount=amount):
                expenses = []
                with self.assertRaisesRegex(ValueError, "greater than zero"):
                    add_expense(expenses, "Bus fare", amount)
                self.assertEqual(expenses, [])

    def test_total_is_zero_when_there_are_no_expenses(self):
        self.assertEqual(calculate_total([]), 0.0)

    def test_total_sums_all_expenses(self):
        expenses = [
            {"description": "Bus fare", "amount": 2.5},
            {"description": "Lunch", "amount": 10.25},
        ]
        self.assertEqual(calculate_total(expenses), 12.75)


if __name__ == "__main__":
    unittest.main()

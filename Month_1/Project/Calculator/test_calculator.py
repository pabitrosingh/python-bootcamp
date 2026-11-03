import unittest

from calculator import calculate


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(2, "+", 3), 5)

    def test_subtraction(self):
        self.assertEqual(calculate(2, "-", 5), -3)

    def test_multiplication(self):
        self.assertEqual(calculate(2.5, "*", 4), 10)

    def test_division(self):
        self.assertEqual(calculate(7, "/", 2), 3.5)

    def test_division_by_zero(self):
        with self.assertRaisesRegex(ZeroDivisionError, "Cannot divide by zero"):
            calculate(7, "/", 0)

    def test_unsupported_operation(self):
        with self.assertRaisesRegex(ValueError, "Choose one of"):
            calculate(1, "%", 2)


if __name__ == "__main__":
    unittest.main()

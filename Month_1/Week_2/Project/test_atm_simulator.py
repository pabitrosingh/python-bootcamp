import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("atm_simulator.py")


class ATMSimulatorTests(unittest.TestCase):
    def run_atm(self, user_input):
        return subprocess.run(
            [sys.executable, str(SCRIPT)],
            input=user_input,
            text=True,
            capture_output=True,
            check=True,
        ).stdout

    def test_check_balance(self):
        output = self.run_atm("1\n")
        self.assertIn("Current balance: $100.00", output)

    def test_deposit(self):
        output = self.run_atm("2\n25.5\n")
        self.assertIn("Deposit approved. New balance: $125.50", output)

    def test_withdrawal(self):
        output = self.run_atm("3\n25\n")
        self.assertIn("Withdrawal approved. New balance: $75.00", output)

    def test_withdrawal_larger_than_balance_is_rejected(self):
        output = self.run_atm("3\n150\n")
        self.assertIn("Insufficient funds. Balance unchanged.", output)

    def test_zero_deposit_is_rejected(self):
        output = self.run_atm("2\n0\n")
        self.assertIn("greater than zero. Balance unchanged.", output)

    def test_negative_withdrawal_is_rejected(self):
        output = self.run_atm("3\n-5\n")
        self.assertIn("greater than zero. Balance unchanged.", output)

    def test_unknown_action_is_rejected(self):
        output = self.run_atm("9\n")
        self.assertIn("Unknown option. Choose 1, 2, or 3.", output)


if __name__ == "__main__":
    unittest.main()

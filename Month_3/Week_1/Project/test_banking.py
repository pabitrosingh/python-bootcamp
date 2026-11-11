import unittest
from datetime import timezone
from decimal import Decimal

from Month_3.Week_1.Project.banking import (
    AccountNotFoundError,
    Bank,
    BankAccount,
    DuplicateAccountError,
    InsufficientFundsError,
    InvalidAmountError,
)


class BankAccountTests(unittest.TestCase):
    def test_deposit_withdraw_and_record_transactions(self):
        account = BankAccount("A-1", "Ada", "10.00")
        account.deposit("2.50")
        account.withdraw("3")

        self.assertEqual(account.balance, Decimal("9.50"))
        self.assertEqual(
            [transaction.kind for transaction in account.transactions],
            ["deposit", "withdrawal"],
        )
        self.assertTrue(
            all(transaction.created_at.tzinfo == timezone.utc
                for transaction in account.transactions)
        )

    def test_rejects_non_positive_or_non_finite_amounts(self):
        account = BankAccount("A-1", "Ada")
        for amount in ("0", "-1", "NaN", "Infinity", "not money"):
            with self.subTest(amount=amount):
                with self.assertRaises(InvalidAmountError):
                    account.deposit(amount)
        self.assertEqual(account.balance, Decimal("0"))

    def test_failed_withdrawal_does_not_change_balance(self):
        account = BankAccount("A-1", "Ada", "5")
        with self.assertRaises(InsufficientFundsError):
            account.withdraw("6")
        self.assertEqual(account.balance, Decimal("5"))
        self.assertEqual(account.transactions, ())

    def test_transfer_updates_both_accounts(self):
        source = BankAccount("A-1", "Ada", "12")
        destination = BankAccount("B-1", "Grace")

        source.transfer_to(destination, "7.25")

        self.assertEqual(source.balance, Decimal("4.75"))
        self.assertEqual(destination.balance, Decimal("7.25"))

    def test_transfer_rejects_same_account(self):
        account = BankAccount("A-1", "Ada", "12")
        with self.assertRaises(ValueError):
            account.transfer_to(account, "1")
        self.assertEqual(account.balance, Decimal("12"))

    def test_transaction_history_is_read_only(self):
        account = BankAccount("A-1", "Ada")
        account.deposit("1")
        history = account.transactions
        self.assertIsInstance(history, tuple)
        self.assertEqual(len(history), 1)


class BankTests(unittest.TestCase):
    def test_account_numbers_are_unique_and_missing_accounts_are_explicit(self):
        bank = Bank()
        account = bank.open_account("A-1", "Ada")

        self.assertIs(bank.get_account("A-1"), account)
        with self.assertRaises(DuplicateAccountError):
            bank.open_account("A-1", "Grace")
        with self.assertRaises(AccountNotFoundError):
            bank.get_account("missing")


if __name__ == "__main__":
    unittest.main()

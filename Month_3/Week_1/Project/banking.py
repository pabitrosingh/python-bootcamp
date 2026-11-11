"""A small in-memory banking domain model."""

from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
import logging


logger = logging.getLogger(__name__)


class BankError(Exception):
    """Base class for expected banking errors."""


class InvalidAmountError(BankError, ValueError):
    """Raised when a money amount is invalid."""


class InsufficientFundsError(BankError):
    """Raised when an account cannot cover a withdrawal."""


class AccountNotFoundError(BankError, LookupError):
    """Raised when an account number is not present."""


class DuplicateAccountError(BankError):
    """Raised when an account number is already in use."""


def _amount(value: Decimal | str | int, *, allow_zero: bool = False) -> Decimal:
    try:
        amount = Decimal(str(value))
    except (InvalidOperation, ValueError) as error:
        raise InvalidAmountError("amount must be a finite decimal value") from error
    if not amount.is_finite() or amount < 0 or (amount == 0 and not allow_zero):
        requirement = "non-negative" if allow_zero else "positive"
        raise InvalidAmountError(f"amount must be finite and {requirement}")
    return amount


@dataclass(frozen=True)
class Transaction:
    kind: str
    amount: Decimal
    created_at: datetime


class BankAccount:
    """Account whose balance can only change through validated operations."""

    def __init__(
        self,
        account_number: str,
        owner: str,
        opening_balance: Decimal | str | int = Decimal("0"),
    ) -> None:
        account_number = account_number.strip()
        owner = owner.strip()
        if not account_number or not owner:
            raise ValueError("account number and owner are required")
        self.account_number = account_number
        self.owner = owner
        self._balance = _amount(opening_balance, allow_zero=True)
        self._transactions: list[Transaction] = []

    @property
    def balance(self) -> Decimal:
        return self._balance

    @property
    def transactions(self) -> tuple[Transaction, ...]:
        return tuple(self._transactions)

    def deposit(self, amount: Decimal | str | int) -> Decimal:
        value = _amount(amount)
        self._balance += value
        self._record("deposit", value)
        logger.info("Deposit recorded", extra={"account_number": self.account_number})
        return self._balance

    def withdraw(self, amount: Decimal | str | int) -> Decimal:
        value = _amount(amount)
        if value > self._balance:
            raise InsufficientFundsError("withdrawal exceeds available balance")
        self._balance -= value
        self._record("withdrawal", value)
        logger.info("Withdrawal recorded", extra={"account_number": self.account_number})
        return self._balance

    def transfer_to(
        self, destination: "BankAccount", amount: Decimal | str | int
    ) -> None:
        if destination is self:
            raise ValueError("source and destination accounts must differ")
        value = _amount(amount)
        self.withdraw(value)
        destination.deposit(value)
        logger.info(
            "Transfer completed",
            extra={
                "source_account": self.account_number,
                "destination_account": destination.account_number,
            },
        )

    def _record(self, kind: str, amount: Decimal) -> None:
        self._transactions.append(
            Transaction(kind, amount, datetime.now(timezone.utc))
        )


class Bank:
    """Registry for in-memory bank accounts."""

    def __init__(self) -> None:
        self._accounts: dict[str, BankAccount] = {}

    def open_account(
        self,
        account_number: str,
        owner: str,
        opening_balance: Decimal | str | int = Decimal("0"),
    ) -> BankAccount:
        number = account_number.strip()
        if number in self._accounts:
            raise DuplicateAccountError(f"account {number!r} already exists")
        account = BankAccount(number, owner, opening_balance)
        self._accounts[number] = account
        return account

    def get_account(self, account_number: str) -> BankAccount:
        try:
            return self._accounts[account_number]
        except KeyError as error:
            raise AccountNotFoundError(
                f"account {account_number!r} was not found"
            ) from error


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    bank = Bank()
    account = bank.open_account("A-100", "Ada", "100.00")
    account.deposit("25.00")
    print(f"{account.owner}'s balance: ${account.balance}")


if __name__ == "__main__":
    main()

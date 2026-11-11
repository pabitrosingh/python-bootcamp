"""An in-memory inventory service with a replaceable product repository."""

from dataclasses import dataclass, replace
from decimal import Decimal, InvalidOperation
import logging
from typing import Protocol


logger = logging.getLogger(__name__)


class InventoryError(Exception):
    """Base class for expected inventory failures."""


class ProductNotFoundError(InventoryError, LookupError):
    """Raised when an SKU is not in the inventory."""


class DuplicateProductError(InventoryError):
    """Raised when an SKU is already registered."""


class InvalidProductError(InventoryError, ValueError):
    """Raised when product data or a quantity is invalid."""


class InsufficientStockError(InventoryError):
    """Raised when a sale exceeds available stock."""


def _price(value: Decimal | str | int) -> Decimal:
    try:
        price = Decimal(str(value))
    except (InvalidOperation, ValueError) as error:
        raise InvalidProductError("unit price must be a finite decimal") from error
    if not price.is_finite() or price < 0:
        raise InvalidProductError("unit price must be finite and non-negative")
    return price


def _quantity(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise InvalidProductError("quantity must be a non-negative whole number")
    return value


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    unit_price: Decimal
    quantity: int


class ProductRepository(Protocol):
    def get(self, sku: str) -> Product | None: ...

    def save(self, product: Product) -> None: ...

    def list_all(self) -> list[Product]: ...


class InMemoryProductRepository:
    """Dictionary-backed repository; contents are not persistent."""

    def __init__(self) -> None:
        self._products: dict[str, Product] = {}

    def get(self, sku: str) -> Product | None:
        return self._products.get(sku)

    def save(self, product: Product) -> None:
        self._products[product.sku] = product

    def list_all(self) -> list[Product]:
        return sorted(self._products.values(), key=lambda product: product.sku)


class InventoryService:
    def __init__(self, repository: ProductRepository) -> None:
        self._repository = repository

    def register_product(
        self,
        sku: str,
        name: str,
        unit_price: Decimal | str | int,
        quantity: int = 0,
    ) -> Product:
        product_sku = sku.strip().upper()
        product_name = name.strip()
        if not product_sku or not product_name:
            raise InvalidProductError("SKU and product name are required")
        if self._repository.get(product_sku) is not None:
            raise DuplicateProductError(f"SKU {product_sku!r} already exists")
        product = Product(
            product_sku,
            product_name,
            _price(unit_price),
            _quantity(quantity),
        )
        self._repository.save(product)
        logger.info("Product registered", extra={"sku": product_sku})
        return product

    def get_product(self, sku: str) -> Product:
        product = self._repository.get(sku.strip().upper())
        if product is None:
            raise ProductNotFoundError(f"SKU {sku!r} was not found")
        return product

    def receive_stock(self, sku: str, quantity: int) -> Product:
        amount = self._positive_quantity(quantity)
        product = self.get_product(sku)
        updated = replace(product, quantity=product.quantity + amount)
        self._repository.save(updated)
        logger.info("Stock received", extra={"sku": product.sku, "quantity": amount})
        return updated

    def sell(self, sku: str, quantity: int) -> Product:
        amount = self._positive_quantity(quantity)
        product = self.get_product(sku)
        if amount > product.quantity:
            raise InsufficientStockError(f"not enough stock for SKU {product.sku!r}")
        updated = replace(product, quantity=product.quantity - amount)
        self._repository.save(updated)
        logger.info("Stock sold", extra={"sku": product.sku, "quantity": amount})
        return updated

    def inventory_value(self) -> Decimal:
        return sum(
            (
                product.unit_price * product.quantity
                for product in self._repository.list_all()
            ),
            start=Decimal("0"),
        )

    @staticmethod
    def _positive_quantity(value: int) -> int:
        amount = _quantity(value)
        if amount == 0:
            raise InvalidProductError("operation quantity must be positive")
        return amount


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    inventory = InventoryService(InMemoryProductRepository())
    inventory.register_product("P-100", "Notebook", "3.25", quantity=8)
    inventory.sell("P-100", 2)
    print(f"Inventory value: ${inventory.inventory_value():.2f}")


if __name__ == "__main__":
    main()

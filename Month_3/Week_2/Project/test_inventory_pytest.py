from decimal import Decimal

import pytest

from Month_3.Week_2.Project.inventory import (
    InMemoryProductRepository,
    InsufficientStockError,
    InventoryService,
    InvalidProductError,
)


@pytest.fixture
def inventory():
    return InventoryService(InMemoryProductRepository())


def test_sale_updates_stock_and_inventory_value(inventory):
    inventory.register_product("P-1", "Notebook", "2.50", quantity=5)

    updated = inventory.sell("P-1", 2)

    assert updated.quantity == 3
    assert inventory.inventory_value() == Decimal("7.50")


@pytest.mark.parametrize("price", ["-1", "NaN", "Infinity"])
def test_invalid_prices_are_rejected(inventory, price):
    with pytest.raises(InvalidProductError):
        inventory.register_product("P-1", "Notebook", price)


def test_sale_cannot_exceed_available_stock(inventory):
    inventory.register_product("P-1", "Notebook", "2", quantity=1)

    with pytest.raises(InsufficientStockError):
        inventory.sell("P-1", 2)

    assert inventory.get_product("P-1").quantity == 1

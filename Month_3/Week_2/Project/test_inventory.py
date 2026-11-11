import unittest
from decimal import Decimal

from Month_3.Week_2.Project.inventory import (
    DuplicateProductError,
    InMemoryProductRepository,
    InsufficientStockError,
    InventoryService,
    InvalidProductError,
    ProductNotFoundError,
)


class InventoryServiceTests(unittest.TestCase):
    def setUp(self):
        self.repository = InMemoryProductRepository()
        self.inventory = InventoryService(self.repository)

    def test_register_product_normalizes_sku_and_name(self):
        product = self.inventory.register_product(" p-1 ", " Notebook ", "1.25", 4)
        self.assertEqual(product.sku, "P-1")
        self.assertEqual(product.name, "Notebook")
        self.assertEqual(product.unit_price, Decimal("1.25"))
        self.assertEqual(self.inventory.get_product("p-1"), product)

    def test_rejects_duplicate_and_invalid_products(self):
        self.inventory.register_product("P-1", "Notebook", "1.25")
        with self.assertRaises(DuplicateProductError):
            self.inventory.register_product("p-1", "Other", "2")
        for args in [
            (" ", "Notebook", "1"),
            ("P-2", " ", "1"),
            ("P-3", "Bad price", "NaN"),
            ("P-4", "Bad quantity", "1", -1),
        ]:
            with self.subTest(args=args), self.assertRaises(InvalidProductError):
                self.inventory.register_product(*args)

    def test_receive_and_sell_stock(self):
        self.inventory.register_product("P-1", "Notebook", "2", quantity=3)
        received = self.inventory.receive_stock("P-1", 4)
        sold = self.inventory.sell("p-1", 2)
        self.assertEqual(received.quantity, 7)
        self.assertEqual(sold.quantity, 5)

    def test_invalid_or_excess_sale_does_not_change_stock(self):
        self.inventory.register_product("P-1", "Notebook", "2", quantity=3)
        for quantity in (0, -1, True):
            with self.subTest(quantity=quantity), self.assertRaises(InvalidProductError):
                self.inventory.sell("P-1", quantity)
        with self.assertRaises(InsufficientStockError):
            self.inventory.sell("P-1", 4)
        self.assertEqual(self.inventory.get_product("P-1").quantity, 3)

    def test_missing_product_is_explicit(self):
        with self.assertRaises(ProductNotFoundError):
            self.inventory.get_product("missing")

    def test_inventory_value_is_decimal_and_empty_value_is_zero(self):
        self.assertEqual(self.inventory.inventory_value(), Decimal("0"))
        self.inventory.register_product("P-1", "Notebook", "2.50", quantity=3)
        self.inventory.register_product("P-2", "Pen", "0.75", quantity=4)
        self.assertEqual(self.inventory.inventory_value(), Decimal("10.50"))

    def test_products_are_returned_in_sku_order(self):
        self.inventory.register_product("B", "B product", "1")
        self.inventory.register_product("A", "A product", "1")
        self.assertEqual(
            [product.sku for product in self.repository.list_all()],
            ["A", "B"],
        )


if __name__ == "__main__":
    unittest.main()

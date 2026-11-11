# Project - Inventory Management System

Build a small in-memory inventory service that validates stock operations and calculates inventory value. The service uses a repository collaborator so business rules can be tested independently from storage.

The reference implementation is [`inventory.py`](./inventory.py), with acceptance tests in [`test_inventory.py`](./test_inventory.py).

## Features

- Register products with unique SKUs, a name, unit price, and initial quantity
- Receive and sell positive whole-number quantities
- Reject duplicate products, unknown SKUs, invalid values, and sales that exceed stock
- Calculate total inventory value using `Decimal`
- Store products through a small repository interface
- Log successful inventory operations without configuring logging in the service

## Run

From the repository root:

```bash
python -m Month_3.Week_2.Project.inventory
python -m unittest -v Month_3.Week_2.Project.test_inventory
python -m pytest -v Month_3.Week_2.Project/test_inventory_pytest.py
```

The project tests use `unittest` and the standard library. If pytest is installed, pytest can run these tests too.
[`test_inventory_pytest.py`](./test_inventory_pytest.py) demonstrates pytest fixtures, parametrization, and plain assertions.

## Acceptance checklist

- [ ] Product SKUs are unique and normalized.
- [ ] Product quantity cannot become negative.
- [ ] Invalid operations do not mutate stock.
- [ ] Inventory totals use decimal arithmetic.
- [ ] `InventoryService` works with the supplied in-memory repository.
- [ ] All tests pass.

## Extensions

- Add a second repository implementation and test the service against it.
- Add reorder thresholds and a report that lists low-stock products.
- Add persistence in Month 4; keep it outside the product model.

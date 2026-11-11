# Week 2 / Example 3 - A focused `unittest` test

Test a function's result directly, rather than testing its implementation details:

```python
import unittest


def discount(price, percent):
    if price < 0 or not 0 <= percent <= 100:
        raise ValueError("invalid price or percent")
    return price * (1 - percent / 100)


class DiscountTests(unittest.TestCase):
    def test_applies_percentage(self):
        self.assertAlmostEqual(discount(80, 25), 60)

    def test_rejects_invalid_percentage(self):
        with self.assertRaises(ValueError):
            discount(80, 120)


if __name__ == "__main__":
    unittest.main()
```

Save this as `test_discount.py` and run `python -m unittest -v test_discount.py`. The `unittest` runner supports test methods named `test_*`; assertions such as `assertAlmostEqual` and `assertRaises` provide useful failure messages.

**Try it:** Add a test for a 0% discount and for a negative price.

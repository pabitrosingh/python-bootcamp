# Week 2 / Example 4 - pytest-style tests

pytest can discover plain test functions and provides concise assertions:

```python
def discount(price, percent):
    if price < 0 or not 0 <= percent <= 100:
        raise ValueError("invalid price or percent")
    return price * (1 - percent / 100)


def test_applies_percentage():
    assert discount(80, 25) == 60


def test_rejects_invalid_percentage():
    import pytest

    with pytest.raises(ValueError):
        discount(80, 120)
```

Save the file as `test_discount.py`; after installing pytest, run `python -m pytest -v`. pytest can also collect tests written with `unittest.TestCase`. Use `@pytest.mark.parametrize` when several inputs should exercise the same behavior. Pytest is not part of Python's standard library, so a project that uses it should declare or document that development dependency.

**Try it:** Parameterize the valid percentages `0`, `25`, and `100`. Keep the expected result next to each input.

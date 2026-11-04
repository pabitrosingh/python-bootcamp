# Week 2 / Example 3 - Dictionary lookup and update

A dictionary maps keys to values. A key must be unique and hashable; strings are a common choice.

```python
stock = {"notebook": 12, "pen": 30}
print(stock["notebook"])
print(stock.get("eraser", 0))  # fallback; does not add "eraser"

stock["pen"] = 28
stock["eraser"] = 10
del stock["notebook"]
```

`stock["missing"]` raises `KeyError`. Use `in` to check a key or use `get()` when an absent key has a useful default.

```python
for item, quantity in stock.items():
    print(f"{item}: {quantity}")
```

**Try it:** Count the occurrences of each word in a short sentence by updating a dictionary in a loop.
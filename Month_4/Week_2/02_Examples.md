# Week 2 / Example 2 - Path and query parameters

FastAPI converts route variables and query strings into Python function arguments:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    result = {"item_id": item_id}
    if q:
        result["q"] = q
    return result
```

This route accepts a numeric `item_id` from the URL and an optional `q` value as a query parameter. Example: `/items/42?q=blue`.

**Try it:** Add a route for `/users/{user_id}/orders` and support a `status` query parameter.

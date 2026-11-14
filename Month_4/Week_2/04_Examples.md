# Week 2 / Example 4 - Handling errors and HTTP status codes

FastAPI allows you to return a custom status code or raise a known HTTP exception:

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

items = {"1": "apple", "2": "banana"}


@app.get("/items/{item_id}")
def get_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )
    return {"item_id": item_id, "value": items[item_id]}
```

This is the web-service equivalent of defensive validation: the server rejects invalid input or missing resources with meaningful API feedback.

**Try it:** Add a POST route that raises `400` if the title is empty and `201` when creation succeeds.

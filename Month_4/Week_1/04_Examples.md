# Week 1 / Example 4 - Status codes and validation checks

API clients need clear feedback. A few common status codes are:

- `200 OK` → success
- `201 Created` → newly created resource
- `400 Bad Request` → invalid input
- `404 Not Found` → resource missing
- `500 Internal Server Error` → unexpected failure

```python

def create_task(title: str):
    if not title or not title.strip():
        raise ValueError("title is required")
    return {"id": 1, "title": title.strip(), "done": False}


try:
    task = create_task("  ")
except ValueError as exc:
    print(f"400 Bad Request: {exc}")
else:
    print(task)
```

This pattern is the same one a FastAPI endpoint will use: validate input first, return a structured payload, and respond with the correct status code.

**Try it:** Add handling for empty descriptions and duplicate task IDs in a mini service function.

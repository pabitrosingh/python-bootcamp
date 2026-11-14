# Week 2 / Example 3 - Request body validation with Pydantic

Pydantic makes it easy to define the expected JSON structure:

```python
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    done: bool = False


@app.post("/tasks")
def create_task(task: TaskCreate):
    return {
        "message": "task created",
        "task": {
            "title": task.title,
            "description": task.description,
            "done": task.done,
        },
    }
```

If a client sends a missing `title` or a wrong data type, FastAPI responds with a validation error before your function is called.

**Try it:** Create a `UserCreate` model with `name`, `email`, and `age` fields and validate a few example payloads.

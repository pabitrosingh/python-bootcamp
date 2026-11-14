# Week 2 / Example 1 - A minimal FastAPI app

FastAPI apps are usually defined in a single Python module:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
```

Start it with Uvicorn:

```bash
uvicorn main:app --reload
```

After starting, open `http://127.0.0.1:8000/docs` to see the generated Swagger UI.

**Try it:** Add a `/about` route that returns your name and a short description.

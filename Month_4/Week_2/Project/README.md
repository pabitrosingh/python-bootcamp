# Project - Task Management API

Build a REST API for creating, listing, updating, and deleting tasks. This project practices FastAPI routes, Pydantic request validation, HTTP status codes, and dependency injection of an in-memory store.

The app is in [`task_api.py`](./task_api.py), with endpoint tests in [`test_task_api.py`](./test_task_api.py).

## Install and run

From the repository root, install [Month 4 dependencies](../../requirements.txt), then run:

```bash
python -m pip install -r Month_4/requirements.txt
python -m uvicorn Month_4.Week_2.Project.task_api:app --reload
```

Open `http://127.0.0.1:8000/docs` to explore the generated OpenAPI documentation. Run tests with:

```bash
python -m unittest -v Month_4.Week_2.Project.test_task_api
```

The store is intentionally in memory so the project can focus on HTTP and validation. Data is reset when the process restarts; the Blog Platform and CRM projects introduce persistence.

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/tasks` | Create a task |
| `GET` | `/tasks` | List tasks; optionally filter with `?completed=true` |
| `GET` | `/tasks/{task_id}` | Get one task |
| `PATCH` | `/tasks/{task_id}` | Update supplied fields |
| `DELETE` | `/tasks/{task_id}` | Delete one task |

## Acceptance checklist

- [ ] New tasks receive unique integer IDs and default to incomplete.
- [ ] Invalid or blank titles are rejected by request validation.
- [ ] Unknown task IDs return HTTP 404.
- [ ] Partial updates change only supplied fields.
- [ ] Deleting a task returns HTTP 204 and subsequent reads return 404.
- [ ] Tests use FastAPI's `TestClient` and do not start a network server.

## References

- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)
- [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/)

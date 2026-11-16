# Project - CRM Backend

Build a customer relationship API with SQLAlchemy 2.x and SQLite. Customers can have notes, demonstrating a one-to-many ORM relationship, request validation, scoped database sessions, and transaction handling.

The app and ORM models are in [`crm.py`](./crm.py); API tests are in [`test_crm.py`](./test_crm.py).

## Install and run

From the repository root, install [Month 4 dependencies](../../requirements.txt), then run:

```bash
python -m pip install -r Month_4/requirements.txt
python -m uvicorn Month_4.Week_4.Project.crm:app --reload
```

By default, the app creates `crm.db` beside `crm.py` when it starts. Set `CRM_DATABASE_URL` to use another SQLAlchemy database URL. Open `http://127.0.0.1:8000/docs` to explore the API.

Run tests with:

```bash
python -m unittest -v Month_4.Week_4.Project.test_crm
```

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/customers` | Create a customer |
| `GET` | `/customers` | List customers |
| `GET` | `/customers/{customer_id}` | Get one customer |
| `PATCH` | `/customers/{customer_id}` | Update supplied customer fields |
| `DELETE` | `/customers/{customer_id}` | Delete a customer and its notes |
| `POST` | `/customers/{customer_id}/notes` | Add a note to a customer |
| `GET` | `/customers/{customer_id}/notes` | List a customer's notes |

## Acceptance checklist

- [ ] SQLAlchemy declarative models map customers and notes to related tables.
- [ ] Each request receives its own SQLAlchemy `Session`.
- [ ] Duplicate email addresses return HTTP 409.
- [ ] Updating an unknown customer and adding notes to one return HTTP 404.
- [ ] Deleting a customer removes its notes through ORM cascade behavior.
- [ ] Tests use a temporary SQLite database.

## References

- [SQLAlchemy ORM Quick Start](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
- [SQLAlchemy Session Basics](https://docs.sqlalchemy.org/en/20/orm/session_basics.html)
- [SQLAlchemy Basic Relationship Patterns](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html)
- [FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/)

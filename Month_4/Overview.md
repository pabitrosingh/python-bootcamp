# Month 4 - Backend Development

## Goal

Use Python to build web services that expose data through HTTP, validate input, store it in a database, and grow from a simple SQLite workflow to a professional SQLAlchemy-backed API.

By the end of the month, you should be able to:

- Explain how HTTP requests and responses move data between clients and servers
- Design clean RESTful routes for resources such as tasks, users, and orders
- Build APIs with FastAPI and validate request bodies with Pydantic models
- Use SQLite to store application data with SQL statements and transactions
- Map database tables to Python objects with SQLAlchemy ORM
- Build a small API that reads and writes persistent data end-to-end

## Prerequisites

Complete [Month 1](../Month_1/Overview.md), [Month 2](../Month_2/Overview.md), and [Month 3](../Month_3/Overview.md). You should be comfortable with Python functions, collections, exceptions, and object-oriented design before writing web applications.

## Weekly plan

| Week | Focus | Theme |
|---|---|---|
| [Week 1](./Week_1/Week_1_Topics.md) | REST APIs and HTTP fundamentals | Understand the request/response model |
| [Week 2](./Week_2/Week_2_Topics.md) | FastAPI basics | Build clean endpoints and validation |
| [Week 3](./Week_3/Week_3_Topics.md) | SQLite and SQL | Persist application data safely |
| [Week 4](./Week_4/Week_4_Topics.md) | SQLAlchemy ORM | Model data and compose a backend |

Each week includes worked examples, short exercises, and links to the relevant official documentation.

## Suggested toolkit

- Python 3.10+
- FastAPI
- Uvicorn
- SQLite (`sqlite3` standard library)
- SQLAlchemy 2.x
- `python-dotenv` (optional for configuration)

## Official references

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [The Python Language Reference](https://docs.python.org/3/reference/index.html)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [SQLite Tutorial](https://www.sqlite.org/docs.html)
- [SQLAlchemy ORM Quick Start](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)

## Month-end completion checklist

- [ ] I can explain the difference between HTTP methods such as GET, POST, PUT, and DELETE.
- [ ] I can define a resource-oriented route design for a simple application.
- [ ] I can build and run a FastAPI endpoint that validates request data.
- [ ] I can create, read, update, and delete records in SQLite using parameterized SQL.
- [ ] I can describe how SQLAlchemy maps Python classes to database tables.
- [ ] I can explain why using ORM classes and explicit transactions makes application code easier to maintain.

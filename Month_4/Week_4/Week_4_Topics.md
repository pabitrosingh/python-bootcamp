# Week 4 - SQLAlchemy ORM and backend integration

## Learning objectives

By the end of this week, you should be able to map Python classes to database tables with SQLAlchemy, use sessions to create and retrieve records, and explain how an ORM fits into a FastAPI backend.

## Seven-day plan

1. Review the difference between SQL and ORM design
2. Install and configure SQLAlchemy
3. Define SQLAlchemy models and table metadata
4. Use a `Session` to create, read, update, and delete objects
5. Add relationships between models, such as `User` and `Task`
6. Connect ORM models to FastAPI endpoints and service logic
7. Practice a simple API workflow from database to JSON response

## Core ideas

- SQLAlchemy is a Python ORM and query toolkit for interacting with databases.
- A model class describes both the Python object and the corresponding database table.
- A session acts as the unit of work for database operations.
- Relationships express how one table connects to another.
- An ORM helps reduce repetitive SQL, but it is still useful to understand the SQL behind the scenes.
- FastAPI and SQLAlchemy work well together when business logic is separated from HTTP concerns.

## Worked examples

- [Example 1: Define a SQLAlchemy model](./01_Examples.md)
- [Example 2: Create and commit a record](./02_Examples.md)
- [Example 3: Query records and filter them](./03_Examples.md)
- [Example 4: Build a small relationship between models](./04_Examples.md)

## Project

Build the [CRM Backend](./Project/README.md) with SQLAlchemy 2.x models, a one-to-many customer/notes relationship, and database-backed API routes.

## Official references

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [The Python Language Reference](https://docs.python.org/3/reference/index.html)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [SQLAlchemy ORM Quick Start](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
- [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/index.html)

## Checklist

- [ ] I can explain the purpose of a SQLAlchemy model.
- [ ] I can describe the role of a Session object in database writes.
- [ ] I can create a relationship between two models and query related records.
- [ ] I can see how FastAPI routes can return ORM data as JSON.

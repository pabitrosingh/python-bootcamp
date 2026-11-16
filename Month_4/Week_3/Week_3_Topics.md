# Week 3 - SQLite and SQL fundamentals

## Learning objectives

By the end of this week, you should be able to create a SQLite database, write SQL statements to create tables and query data, and understand how a backend uses a database to persist application state.

## Seven-day plan

1. Learn what SQLite is and why it is useful for local and small web apps
2. Connect to a database with Python's `sqlite3` module
3. Create tables and define primary keys and constraints
4. Insert, update, and delete records safely with SQL statements
5. Query rows with `SELECT` and filter results using `WHERE`
6. Use transactions and parameterized queries for safer code
7. Practice a CRUD workflow for tasks, blog posts, or customers

## Core ideas

- SQLite is a serverless, file-based database that is easy to use in Python projects.
- A table defines a collection of related records, and each row is a single record.
- SQL statements let you create data, read it, modify it, and delete it.
- Parameterized queries help avoid SQL injection and keep values safe.
- Transactions make multi-step changes reliable: either all changes commit or none do.
- A web API often stores data in a database rather than keeping everything in memory.

## Worked examples

- [Example 1: Create a SQLite database and connect](./01_Examples.md)
- [Example 2: Create a table and insert rows](./02_Examples.md)
- [Example 3: Query and filter tasks](./03_Examples.md)
- [Example 4: Update and delete records](./04_Examples.md)

## Project

Build the [Blog Platform](./Project/README.md), a CRUD API backed by SQLite with parameterized SQL and explicit transaction boundaries.

## Official references

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [The Python Language Reference](https://docs.python.org/3/reference/index.html)
- [Python `sqlite3` documentation](https://docs.python.org/3/library/sqlite3.html)
- [SQLite SQL documentation](https://www.sqlite.org/lang.html)
- [SQLite tutorial](https://www.sqlite.org/quickstart.html)

## Checklist

- [ ] I can connect to a SQLite database file from Python.
- [ ] I can create a table with sensible columns and primary keys.
- [ ] I can use `INSERT`, `SELECT`, `UPDATE`, and `DELETE` statements.
- [ ] I can explain why parameterized SQL is safer than string interpolation.

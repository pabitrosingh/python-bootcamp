# Week 3 / Example 1 - Create a SQLite database and connect

Python's standard library includes everything needed to work with SQLite:

```python
import sqlite3

connection = sqlite3.connect('app.db')
cursor = connection.cursor()
print('Connected to SQLite')

cursor.execute('SELECT sqlite_version();')
print(cursor.fetchone())

connection.close()
```

The database is stored as a local file (`app.db`), which makes it convenient for prototypes, small services, and local development.

**Try it:** Create a database file called `tasks.db` and print the SQLite version.

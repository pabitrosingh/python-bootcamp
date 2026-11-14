# Week 3 / Example 2 - Create a table and insert rows

```python
import sqlite3

connection = sqlite3.connect('tasks.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        done INTEGER DEFAULT 0
    )
''')

cursor.execute(
    'INSERT INTO tasks (title, description, done) VALUES (?, ?, ?)',
    ('Write API notes', 'Review FastAPI and SQLite concepts', 0),
)
connection.commit()
print('Inserted task')
connection.close()
```

This uses SQL to define a table and a parameterized insert to keep the statement safe and readable.

**Try it:** Add a second task and inspect the rows with `SELECT * FROM tasks`.

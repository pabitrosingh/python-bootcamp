# Week 3 / Example 3 - Query and filter tasks

```python
import sqlite3

connection = sqlite3.connect('tasks.db')
cursor = connection.cursor()

cursor.execute('SELECT id, title, done FROM tasks WHERE done = 0 ORDER BY id')
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()
```

This shows the shape of real application code: query data, transform the rows into Python objects, and then return them from an API or service layer.

**Try it:** Add a `WHERE title LIKE ?` filter to search for tasks with a keyword in the title.

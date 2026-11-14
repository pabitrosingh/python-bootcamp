# Week 3 / Example 4 - Update and delete records

```python
import sqlite3

connection = sqlite3.connect('tasks.db')
cursor = connection.cursor()

cursor.execute('UPDATE tasks SET done = 1 WHERE title = ?', ('Write API notes',))
cursor.execute('DELETE FROM tasks WHERE done = 1 AND id = 2')
connection.commit()

print('Updated and deleted rows')
connection.close()
```

Transactions make it cleaner to update multiple related changes as one logical unit. If an error happens before `commit()`, the database keeps the previous state intact.

**Try it:** Wrap a small sequence of inserts and updates in a `try/except` block so failed writes roll back cleanly.

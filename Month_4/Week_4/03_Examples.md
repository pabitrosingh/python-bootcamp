# Week 4 / Example 3 - Query records and filter them

```python
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///tasks.db')

with Session(engine) as session:
    stmt = select(Task).where(Task.done.is_(False)).order_by(Task.id)
    pending_tasks = session.execute(stmt).scalars().all()

    for task in pending_tasks:
        print(task.id, task.title, task.done)
```

The query API is Pythonic and expressive. SQLAlchemy builds the right SQL for you while still exposing the underlying relational model.

**Try it:** Add a `where(Task.title.contains('api'))` filter and print the matching tasks.

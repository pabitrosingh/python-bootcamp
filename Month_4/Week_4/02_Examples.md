# Week 4 / Example 2 - Create and commit a record

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///tasks.db')

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = 'tasks'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    done: Mapped[bool] = mapped_column(default=False)


Base.metadata.create_all(engine)

with Session(engine) as session:
    task = Task(title='Refactor user model', done=False)
    session.add(task)
    session.commit()
    print(task.id)
```

The engine handles the database connection, and the session groups writes into one transaction.

**Try it:** Add a second task and print all tasks in the database.

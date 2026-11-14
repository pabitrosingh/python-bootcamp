# Week 4 / Example 1 - Define a SQLAlchemy model

SQLAlchemy models are normal Python classes with table metadata:

```python
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    done: Mapped[bool] = mapped_column(default=False)
```

The class is mapped to a database table. The ORM takes care of translating Python object operations into SQL statements.

**Try it:** Add a `description` column and a `created_at` timestamp field to the model.

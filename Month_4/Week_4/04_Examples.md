# Week 4 / Example 4 - Build a small relationship between models

Relationships connect records across tables:

```python
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    tasks: Mapped[list['Task']] = relationship(back_populates='owner')


class Task(Base):
    __tablename__ = 'tasks'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    owner_id: Mapped[int | None] = mapped_column(ForeignKey('users.id'))
    owner: Mapped['User | None'] = relationship(back_populates='tasks')
```

This pattern is useful for real backend systems when a user has many tasks or a post belongs to a single author.

**Try it:** Add a `Project` model and a one-to-many relationship between a project and its tasks.

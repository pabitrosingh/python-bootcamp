"""A small in-memory task CRUD API built with FastAPI."""

from __future__ import annotations

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field, field_validator, model_validator


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(default="", max_length=2_000)

    @field_validator("title")
    @classmethod
    def strip_title(cls, value: str) -> str:
        title = value.strip()
        if not title:
            raise ValueError("title must not be blank")
        return title


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=2_000)
    completed: bool | None = None

    @field_validator("title")
    @classmethod
    def strip_title(cls, value: str | None) -> str | None:
        if value is None:
            return value
        title = value.strip()
        if not title:
            raise ValueError("title must not be blank")
        return title

    @model_validator(mode="after")
    def validate_patch(self) -> TaskUpdate:
        if not self.model_fields_set:
            raise ValueError("at least one field must be supplied")
        if any(getattr(self, name) is None for name in self.model_fields_set):
            raise ValueError("fields cannot be null")
        return self


class TaskRead(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False


class TaskStore:
    """Simple replaceable store; contents last only for this process."""

    def __init__(self) -> None:
        self._tasks: dict[int, TaskRead] = {}
        self._next_id = 1

    def create(self, task: TaskCreate) -> TaskRead:
        record = TaskRead(id=self._next_id, **task.model_dump())
        self._tasks[record.id] = record
        self._next_id += 1
        return record

    def list(self, completed: bool | None = None) -> list[TaskRead]:
        tasks = sorted(self._tasks.values(), key=lambda task: task.id)
        if completed is None:
            return tasks
        return [task for task in tasks if task.completed is completed]

    def get(self, task_id: int) -> TaskRead | None:
        return self._tasks.get(task_id)

    def update(self, task_id: int, changes: dict[str, object]) -> TaskRead | None:
        task = self._tasks.get(task_id)
        if task is None:
            return None
        updated = task.model_copy(update=changes)
        self._tasks[task_id] = updated
        return updated

    def delete(self, task_id: int) -> bool:
        return self._tasks.pop(task_id, None) is not None


def create_app(store: TaskStore | None = None) -> FastAPI:
    task_store = store if store is not None else TaskStore()
    app = FastAPI(title="Task Management API", version="1.0.0")

    @app.post("/tasks", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
    def create_task(payload: TaskCreate) -> TaskRead:
        return task_store.create(payload)

    @app.get("/tasks", response_model=list[TaskRead])
    def list_tasks(completed: bool | None = None) -> list[TaskRead]:
        return task_store.list(completed)

    @app.get("/tasks/{task_id}", response_model=TaskRead)
    def get_task(task_id: int) -> TaskRead:
        task = task_store.get(task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    @app.patch("/tasks/{task_id}", response_model=TaskRead)
    def update_task(task_id: int, payload: TaskUpdate) -> TaskRead:
        task = task_store.update(task_id, payload.model_dump(exclude_unset=True))
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    @app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_task(task_id: int) -> Response:
        if not task_store.delete(task_id):
            raise HTTPException(status_code=404, detail="Task not found")
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return app


app = create_app()

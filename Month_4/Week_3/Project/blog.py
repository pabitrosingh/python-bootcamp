"""A SQLite-backed blog posts API."""

from __future__ import annotations

from contextlib import asynccontextmanager, contextmanager
from datetime import datetime, timezone
import os
from pathlib import Path
import sqlite3
from collections.abc import AsyncIterator, Iterator

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field, field_validator


class PostInput(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    body: str = Field(min_length=1, max_length=50_000)

    @field_validator("title")
    @classmethod
    def strip_title(cls, value: str) -> str:
        title = value.strip()
        if not title:
            raise ValueError("title must not be blank")
        return title


class PostRead(BaseModel):
    id: int
    title: str
    body: str
    created_at: datetime


class BlogRepository:
    """Owns SQLite connections and parameterized post queries."""

    def __init__(self, database_path: str | Path) -> None:
        self.database_path = Path(database_path)

    @contextmanager
    def _connection(self) -> Iterator[sqlite3.Connection]:
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        try:
            with connection:
                yield connection
        finally:
            connection.close()

    def initialize(self) -> None:
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        with self._connection() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    body TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )

    @staticmethod
    def _to_post(row: sqlite3.Row) -> PostRead:
        return PostRead(
            id=row["id"],
            title=row["title"],
            body=row["body"],
            created_at=datetime.fromisoformat(row["created_at"]),
        )

    def create(self, payload: PostInput) -> PostRead:
        created_at = datetime.now(timezone.utc)
        with self._connection() as connection:
            cursor = connection.execute(
                "INSERT INTO posts (title, body, created_at) VALUES (?, ?, ?)",
                (payload.title, payload.body, created_at.isoformat()),
            )
            post_id = cursor.lastrowid
        if post_id is None:
            raise RuntimeError("SQLite did not return an ID for the created post")
        return PostRead(
            id=post_id,
            title=payload.title,
            body=payload.body,
            created_at=created_at,
        )

    def list(self) -> list[PostRead]:
        with self._connection() as connection:
            rows = connection.execute(
                "SELECT id, title, body, created_at FROM posts ORDER BY id"
            ).fetchall()
        return [self._to_post(row) for row in rows]

    def get(self, post_id: int) -> PostRead | None:
        with self._connection() as connection:
            row = connection.execute(
                "SELECT id, title, body, created_at FROM posts WHERE id = ?",
                (post_id,),
            ).fetchone()
        return self._to_post(row) if row is not None else None

    def update(self, post_id: int, payload: PostInput) -> PostRead | None:
        with self._connection() as connection:
            cursor = connection.execute(
                "UPDATE posts SET title = ?, body = ? WHERE id = ?",
                (payload.title, payload.body, post_id),
            )
            if cursor.rowcount == 0:
                return None
            row = connection.execute(
                "SELECT id, title, body, created_at FROM posts WHERE id = ?",
                (post_id,),
            ).fetchone()
        if row is None:
            return None
        return self._to_post(row)

    def delete(self, post_id: int) -> bool:
        with self._connection() as connection:
            cursor = connection.execute(
                "DELETE FROM posts WHERE id = ?", (post_id,)
            )
            return cursor.rowcount > 0


def create_app(database_path: str | Path | None = None) -> FastAPI:
    default_path = Path(__file__).with_name("blog.db")
    repository = BlogRepository(
        database_path or os.environ.get("BLOG_DATABASE", str(default_path))
    )

    @asynccontextmanager
    async def lifespan(_: FastAPI) -> AsyncIterator[None]:
        repository.initialize()
        yield

    app = FastAPI(title="Blog Platform API", version="1.0.0", lifespan=lifespan)

    @app.post("/posts", response_model=PostRead, status_code=status.HTTP_201_CREATED)
    def create_post(payload: PostInput) -> PostRead:
        return repository.create(payload)

    @app.get("/posts", response_model=list[PostRead])
    def list_posts() -> list[PostRead]:
        return repository.list()

    @app.get("/posts/{post_id}", response_model=PostRead)
    def get_post(post_id: int) -> PostRead:
        post = repository.get(post_id)
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")
        return post

    @app.put("/posts/{post_id}", response_model=PostRead)
    def update_post(post_id: int, payload: PostInput) -> PostRead:
        post = repository.update(post_id, payload)
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")
        return post

    @app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_post(post_id: int) -> Response:
        if not repository.delete(post_id):
            raise HTTPException(status_code=404, detail="Post not found")
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return app


app = create_app()

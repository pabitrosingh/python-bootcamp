# Project - Blog Platform

Build a small posts API backed by SQLite. This project practices table creation, parameterized SQL, transactions, resource routes, and separating persistence code from HTTP handling.

The app and repository are in [`blog.py`](./blog.py); endpoint tests are in [`test_blog.py`](./test_blog.py).

## Install and run

From the repository root, install [Month 4 dependencies](../../requirements.txt), then run:

```bash
python -m pip install -r Month_4/requirements.txt
python -m uvicorn Month_4.Week_3.Project.blog:app --reload
```

By default, the app creates `blog.db` beside `blog.py` when it starts. Set `BLOG_DATABASE` to use another database file. Open `http://127.0.0.1:8000/docs` to explore the API.

Run tests with:

```bash
python -m unittest -v Month_4.Week_3.Project.test_blog
```

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/posts` | Create a post |
| `GET` | `/posts` | List posts |
| `GET` | `/posts/{post_id}` | Get one post |
| `PUT` | `/posts/{post_id}` | Replace a post's title and body |
| `DELETE` | `/posts/{post_id}` | Delete one post |

## Acceptance checklist

- [ ] Post data persists across app instances using the same SQLite file.
- [ ] SQL values are passed as bound parameters, not interpolated into query strings.
- [ ] Each write runs in a transaction and rolls back if it fails.
- [ ] Missing posts return HTTP 404.
- [ ] Tests use a temporary database and do not touch the default database file.

## References

- [Python `sqlite3` tutorial](https://docs.python.org/3/library/sqlite3.html#tutorial)
- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)
- [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [SQLite language reference](https://www.sqlite.org/lang.html)

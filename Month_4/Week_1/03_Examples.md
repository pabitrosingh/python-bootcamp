# Week 1 / Example 3 - REST route design for a task app

A REST API usually exposes resources at stable URLs. For a task manager, a clean design might look like this:

- `GET /tasks` → list all tasks
- `POST /tasks` → create a new task
- `GET /tasks/1` → fetch one task
- `PUT /tasks/1` → replace a task
- `PATCH /tasks/1` → update part of a task
- `DELETE /tasks/1` → delete a task

The route names use nouns, not actions. "Get tasks" is represented by `GET /tasks`, not `/get_tasks`.

**Try it:** Design a small blog API with routes for posts and comments. Decide which actions belong under each resource.

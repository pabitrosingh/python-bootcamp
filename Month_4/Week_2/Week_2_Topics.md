# Week 2 - FastAPI basics

## Learning objectives

By the end of this week, you should be able to create a minimal FastAPI app, define routes, accept query parameters and JSON bodies, and validate input with model classes.

## Seven-day plan

1. Install FastAPI and Uvicorn locally
2. Understand the `app = FastAPI()` pattern
3. Build simple GET and POST routes
4. Use path parameters and query parameters
5. Validate request payloads with Pydantic models
6. Explore Swagger UI and OpenAPI docs that FastAPI generates automatically
7. Practice building a small CRUD API for one resource

## Core ideas

- FastAPI is a modern Python web framework built for APIs.
- Route functions are usually plain Python functions with type hints and decorators.
- FastAPI reads request data and validates it before it reaches your logic.
- Pydantic models define the expected shape of request bodies.
- OpenAPI makes it easy to generate API docs and client code.
- A route should be focused on one resource and should not mix unrelated behavior.

## Worked examples

- [Example 1: A minimal FastAPI app](./01_Examples.md)
- [Example 2: Path and query parameters](./02_Examples.md)
- [Example 3: Request body validation with Pydantic](./03_Examples.md)
- [Example 4: Handling errors and HTTP status codes](./04_Examples.md)

## Official references

- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Pydantic Docs](https://docs.pydantic.dev/latest/)
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [The Python Language Reference](https://docs.python.org/3/reference/index.html)

## Checklist

- [ ] I can start a FastAPI app and view the generated docs at `/docs`.
- [ ] I can define a route for a collection and a single resource.
- [ ] I can pass path and query parameters into a route function.
- [ ] I can explain how Pydantic models validate incoming JSON.

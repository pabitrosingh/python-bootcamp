# Week 1 - REST APIs and HTTP fundamentals

## Learning objectives

By the end of this week, you should be able to describe how browsers and servers exchange HTTP messages, explain why REST uses resources and nouns, and map common CRUD operations to URLs and HTTP methods.

## Seven-day plan

1. Review HTTP, clients, servers, and request/response cycles
2. Learn the meaning of GET, POST, PUT, PATCH, and DELETE
3. Design resource-oriented URLs for a task or blog application
4. Understand JSON as the standard API payload format
5. Study status codes and error handling for API requests
6. Complete the worked examples and try the small examples locally
7. Reflect on how a REST API differs from a function call in Python

## Core ideas

- HTTP is the protocol that carries requests and responses between clients and servers.
- REST organizes data around resources such as `/tasks`, `/users`, or `/posts` rather than around procedures.
- HTTP methods define intent: GET reads, POST creates, PUT/PATCH updates, and DELETE removes.
- JSON is a compact format for sending structured values between Python apps and browsers.
- Status codes communicate whether a request succeeded, failed, or needs more information.
- A good API keeps its contract predictable and documents which fields are required.

## Worked examples

- [Example 1: A tiny HTTP server in Python](./01_Examples.md)
- [Example 2: JSON serialization and parsing](./02_Examples.md)
- [Example 3: REST route design for a task app](./03_Examples.md)
- [Example 4: Status codes and validation checks](./04_Examples.md)

## Official references

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [The Python Language Reference](https://docs.python.org/3/reference/index.html)
- [MDN: HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [MDN: HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [MDN: Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

## Checklist

- [ ] I can explain what an HTTP request and response contain.
- [ ] I can map CRUD actions to HTTP methods.
- [ ] I can explain why JSON is common in APIs and how it differs from Python objects.
- [ ] I can choose a simple URL structure for a resource-backed app.

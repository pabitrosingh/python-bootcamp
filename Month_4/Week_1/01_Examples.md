# Week 1 / Example 1 - A tiny HTTP server in Python

The standard library has a useful minimal web server for local learning:

```python
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"message": "hello from Python"}')

    def log_message(self, format, *args):
        return


server = HTTPServer(('127.0.0.1', 8000), Handler)
print('Serving on http://127.0.0.1:8000')
server.serve_forever()
```

This is not a production API, but it demonstrates the core pattern: a client sends a request, the server inspects the method and URL, and then returns a response.

**Try it:** Add a `do_POST` method that reads a JSON request body and echoes it back.

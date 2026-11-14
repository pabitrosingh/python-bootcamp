# Week 1 / Example 2 - JSON serialization and parsing

JSON is the standard format for API payloads. Python has a built-in `json` module for conversion between Python data and JSON text:

```python
import json

payload = {
    "title": "Launch checklist",
    "done": False,
    "tags": ["backend", "api"]
}

text = json.dumps(payload)
print(text)
print(type(text))

restored = json.loads(text)
print(restored)
print(type(restored))
```

The `dumps()` function serializes to a JSON string. `loads()` converts JSON text back into Python data. In actual APIs, the server reads incoming JSON bytes and sends JSON text back to the client.

**Try it:** Create a function `to_api_payload(task)` that returns a dictionary with `id`, `title`, and `completed` fields.

# Week 3 / Example 3 - Structured JSON data

JSON is useful for storing simple data structures between program runs:

```python
import json
from pathlib import Path

path = Path("settings.json")
settings = {"theme": "light", "font_size": 14}
path.write_text(json.dumps(settings, indent=2) + "\n", encoding="utf-8")

loaded_settings = json.loads(path.read_text(encoding="utf-8"))
print(loaded_settings["theme"])
```

`json.dump()` and `json.load()` work with open file objects. JSON object keys are strings. Tuples are serialized as JSON arrays and load back as lists; arbitrary Python objects are not automatically supported. Invalid JSON raises `json.JSONDecodeError`.

**Try it:** Save a list of three dictionaries to JSON, read it back, and print one field from each record.
# Week 3 / Example 2 - Write and append

Writing with mode `"w"` replaces existing file contents. Appending with mode `"a"` preserves existing contents and adds data at the end.

```python
from pathlib import Path

path = Path("daily_log.txt")
with path.open("w", encoding="utf-8") as file:
    file.write("First entry\n")

with path.open("a", encoding="utf-8") as file:
    file.write("Another entry\n")
```

For small files, `path.write_text(text, encoding="utf-8")` and `path.read_text(encoding="utf-8")` are concise alternatives. `write_text()` also replaces the old contents.

**Try it:** Write three lines to a file using `writelines()`. Remember that `writelines()` does not add newline characters for you.
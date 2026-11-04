# Week 3 / Example 1 - Read a text file

Use `pathlib.Path` and a context manager for a small UTF-8 file:

```python
from pathlib import Path

path = Path("notes.txt")
with path.open("r", encoding="utf-8") as file:
    text = file.read()

print(text)
```

The `with` block closes the file when it exits. `read()` returns the full contents; `readline()` reads one line; iterating over the file processes lines one at a time.

A missing file raises `FileNotFoundError`, which is an `OSError`. Report a missing input file to the user rather than pretending it was empty. Relative paths are based on the current working directory, not automatically on the script's folder.

**Try it:** Read a text file one line at a time and print line numbers with `enumerate()`.
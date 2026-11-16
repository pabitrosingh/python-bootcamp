# Week 4 / Example 1 - Organize paths with `pathlib`

`Path` offers platform-aware path operations and convenient directory traversal:

```python
from pathlib import Path


directory = Path("reports")
for path in sorted(directory.glob("*.txt")):
    if path.is_file():
        print(path.name, path.stat().st_size)
```

Use `Path` operations such as `/`, `.suffix`, `.glob()`, and `.is_file()` instead of concatenating path strings. Check what a command will touch before adding write or delete behavior.

**Try it:** Write a function that returns all `.csv` files under a directory without opening or modifying them.
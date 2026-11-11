# Week 3 / Example 4 - Standard-library tools

Python's standard library includes modules for common application needs:

```python
from collections import Counter
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path


class Status(Enum):
    PENDING = "pending"
    COMPLETE = "complete"


counts = Counter(["python", "tests", "python"])
now = datetime.now(timezone.utc)
notes_path = Path("notes.txt")

print(counts["python"])
print(now.isoformat())
print(Status.PENDING.value)
print(notes_path.suffix)
```

Use timezone-aware datetimes for instants that cross machine or timezone boundaries. `Path` composes paths without hand-written separators. `Enum` restricts a field to a named set of choices. `Counter` is a dictionary-like tool for counting hashable values.

**Try it:** Use `defaultdict(list)` to group names by their first letter, then compare it with `dict.setdefault`.

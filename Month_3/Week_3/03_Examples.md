# Week 3 / Example 3 - Logging levels and module loggers

Reusable modules should create a named logger and emit events. The application decides where and how those events are displayed:

```python
import logging

logger = logging.getLogger(__name__)


def remove_item(items, item_id):
    try:
        return items.pop(item_id)
    except KeyError:
        logger.warning("Item not found", extra={"item_id": item_id})
        raise
```

`DEBUG` is detailed diagnostic information, `INFO` describes normal milestones, `WARNING` signals an unexpected but recoverable situation, `ERROR` indicates a failed operation, and `CRITICAL` describes a serious failure. Configure logging once at the application entry point, for example with `logging.basicConfig(level=logging.INFO)`. Avoid logging and swallowing the same exception; either handle it or let it propagate with context.

**Try it:** Configure the root logger in a small `main()` function. Run `remove_item` with a missing key and confirm both the warning and the original `KeyError` are visible.

# Week 4 / Example 3 - Log an automation task

Libraries should create a named logger and leave configuration to the application:

```python
import logging


logger = logging.getLogger(__name__)


def process_item(name):
    logger.info("Processing %s", name)
    try:
        return name.strip().upper()
    except AttributeError:
        logger.exception("Could not process item %r", name)
        raise


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    print(process_item(" report "))
```

Parameterized logging avoids eagerly formatting a message when that log level is disabled. `logger.exception()` includes exception details and should be called from an exception handler.

**Try it:** Add a warning when a valid string is empty after stripping.
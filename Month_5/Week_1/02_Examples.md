# Week 1 / Example 2 - A configurable retry decorator

A decorator factory lets a caller configure the decorator:

```python
from functools import wraps
from time import sleep


def retry(attempts, delay=0):
    if attempts < 1:
        raise ValueError("attempts must be at least one")

    def decorate(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for attempt in range(attempts):
                try:
                    return function(*args, **kwargs)
                except (TimeoutError, ConnectionError):
                    if attempt + 1 == attempts:
                        raise
                    sleep(delay)

        return wrapper

    return decorate


@retry(attempts=3, delay=0.1)
def read_service():
    return "ready"


print(read_service())
```

The retry policy handles only the transient exceptions named in its `except` clause. The final failure is re-raised with its original traceback. In production, retries should be bounded and delays should account for the external service's policy.

**Try it:** Count calls to a test function that raises `ConnectionError` twice and succeeds on the third call.
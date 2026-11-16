# Week 4 / Example 4 - Measure elapsed time

Use a monotonic clock for durations:

```python
from time import monotonic, sleep


started = monotonic()
sleep(0.05)
elapsed = monotonic() - started
print(f"Elapsed: {elapsed:.3f} seconds")
```

`monotonic()` cannot go backward due to wall-clock adjustments, making it appropriate for elapsed-time measurement. It does not represent a calendar timestamp; use `datetime` for dates and times intended for people.

**Try it:** Measure a sequential and a concurrent version of a task with the same inputs. Report the inputs and avoid drawing conclusions from tiny, noisy measurements.
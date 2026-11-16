# Week 2 / Example 2 - CPU work with processes

For CPU-heavy pure-Python work, separate processes can use multiple cores:

```python
from concurrent.futures import ProcessPoolExecutor


def sum_squares(stop):
    return sum(number * number for number in range(stop))


def main():
    limits = [100_000, 200_000, 300_000]
    with ProcessPoolExecutor() as executor:
        print(list(executor.map(sum_squares, limits)))


if __name__ == "__main__":
    main()
```

The worker function is defined at module scope so a child process can import it. The guard prevents child processes from rerunning the application's top-level work when the module is imported. Small tasks may be slower in a process pool because starting workers and transferring inputs/results have costs.

**Try it:** Run the same calculation sequentially and compare results first; only use timings for sufficiently large inputs.
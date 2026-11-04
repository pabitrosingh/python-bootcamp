# Week 4 / Example 4 - Choose recursion or iteration

Factorial is defined for non-negative integers: `0!` is `1`, and `n!` is `n * (n - 1)!`.

```python
def factorial_recursive(number):
    if number < 0:
        raise ValueError("number must be non-negative")
    if number == 0:
        return 1
    return number * factorial_recursive(number - 1)


def factorial_iterative(number):
    if number < 0:
        raise ValueError("number must be non-negative")
    result = 1
    for factor in range(2, number + 1):
        result *= factor
    return result
```

Both functions return the same result for ordinary inputs. The iterative version uses constant call-stack space and has no recursion-depth failure. Use recursion when it models the structure clearly; do not use it just because a problem can be expressed recursively.

**Try it:** Test both versions with `0`, `1`, and `5`, then check that both reject `-1`.
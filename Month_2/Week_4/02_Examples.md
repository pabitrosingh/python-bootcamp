# Week 4 / Example 2 - Sum a sequence recursively

Define the sum of an empty list as zero. For a non-empty list, add its first value to the sum of the remaining values:

```python
def recursive_sum(numbers):
    if not numbers:  # base case
        return 0
    return numbers[0] + recursive_sum(numbers[1:])


print(recursive_sum([4, 7, 2]))  # 13
print(recursive_sum([]))         # 0
```

Each call receives a shorter list. This version creates slices, so it is intended for learning rather than large inputs. In everyday Python, `sum(numbers)` is clearer and more efficient.

**Try it:** Add a test for a single-item list and predict the number of recursive calls.
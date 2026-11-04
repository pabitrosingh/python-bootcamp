# Week 4 / Example 1 - Countdown and base cases

A recursive function needs a base case that stops the calls, and a recursive step that moves toward it:

```python
def countdown(number):
    if number <= 0:  # base case
        print("Done")
        return

    print(number)
    countdown(number - 1)  # smaller problem


countdown(3)
```

The calls receive `3`, `2`, `1`, then `0`, where the base case stops. If the argument is not moving toward the base case, the function can keep calling itself until Python raises `RecursionError`.

**Try it:** Trace `countdown(2)` on paper and write the order in which the numbers are printed.
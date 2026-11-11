# Week 3 / Example 1 - Catch a specific exception

Catch an expected conversion error close to the input boundary and retry:

```python
def read_quantity(input_function=input):
    while True:
        try:
            quantity = int(input_function("Quantity: "))
        except ValueError:
            print("Enter a whole number.")
        else:
            if quantity >= 0:
                return quantity
            print("Quantity cannot be negative.")
```

The `except` handles invalid integer text. The `else` runs only when conversion succeeds. Other failures are not swallowed. A function that receives `input_function` can be tested without requiring a person to type at a prompt.

**Try it:** Supply a list-backed fake input function that returns `"nope"` and then `"3"`. Confirm the function returns `3`.

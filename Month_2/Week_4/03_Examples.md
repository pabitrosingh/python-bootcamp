# Week 4 / Example 3 - Reverse a string recursively

For a string of length zero or one, the reversed value is the string itself. Otherwise, reverse the tail and place the first character at the end:

```python
def reverse_text(text):
    if len(text) <= 1:
        return text
    return reverse_text(text[1:]) + text[0]


print(reverse_text("cat"))  # tac
print(reverse_text(""))     # an empty string
```

The input shrinks by one character per call. Repeated slicing and concatenation make this approach inefficient for long strings; `text[::-1]` is the idiomatic solution in real code.

**Try it:** Trace the calls for `"go"` and note when each character is added to the result.
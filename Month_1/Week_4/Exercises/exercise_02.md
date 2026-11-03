# Exercise 2 - Safe whole-number input

Write a function `ask_for_integer(prompt)` that repeatedly asks for input until the user enters a valid whole number. Return the integer; do not print it from inside the function.

Handle `ValueError` and give a helpful retry message.

**Test:** Enter `hello`, then `12`. The function should recover from the first input and return `12`.

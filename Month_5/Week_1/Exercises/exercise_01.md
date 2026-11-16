# Exercise 1 - Decorate a function

Write a `@count_calls` decorator that counts how many times a function is called.

Requirements:

1. The decorated function must accept positional and keyword arguments.
2. The wrapper must return the original result and must not suppress exceptions.
3. Use `functools.wraps`.
4. Expose the count in a documented way, such as a `calls` attribute on the wrapper.

Test it with a function that returns a value and another that raises an exception. Confirm the count increments for both calls.

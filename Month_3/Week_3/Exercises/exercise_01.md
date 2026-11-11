# Exercise 1 - Translate a low-level exception

Write a function that reads UTF-8 text from a path. Translate an `OSError` into a domain-specific `ConfigurationError`, preserving the cause with `raise ... from error`.

**Test:** Verify that a missing file raises `ConfigurationError` and that its `__cause__` is the original `FileNotFoundError`.

**Try next:** Do not translate a decoding error unless the function can add useful context for it too.

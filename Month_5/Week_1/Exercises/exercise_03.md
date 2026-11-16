# Exercise 3 - Stream a text file

Write a generator `iter_words(path)` that reads a UTF-8 text file line by line and yields whitespace-separated words in their original order.

Requirements:

- Use a `with` statement so the file is closed when iteration finishes or the generator is closed.
- Do not read the entire file into memory.
- Ignore blank lines.
- Test an empty file, a line with repeated spaces, and a multi-line file using a temporary directory.

Extension: Add a second generator that yields only words longer than four characters.

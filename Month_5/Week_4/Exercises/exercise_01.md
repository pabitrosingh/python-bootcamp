# Exercise 1 - Preview a file operation

Write a command-line utility that lists files it would move from one directory into subdirectories named for their extensions.

Requirements:

- Use `pathlib`.
- Preview by default.
- Require an explicit `--apply` flag before moving anything.
- Print the source and proposed destination for every file.
- Test the planning function with `tempfile.TemporaryDirectory()`; do not operate on a personal directory.

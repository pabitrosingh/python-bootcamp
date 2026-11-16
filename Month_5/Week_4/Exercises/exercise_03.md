# Exercise 3 - Monitor a temporary directory

Build a polling monitor that records the paths and metadata of files in a directory, then reports files added, modified, or removed between scans.

Requirements:

- Use `Path` for filesystem operations and `time.monotonic()` for elapsed-time logic.
- Keep the snapshot-diffing function separate from the long-running polling loop.
- Test additions, modifications, and removals in a temporary directory.
- Document that polling detects changes with a delay and may not observe every intermediate version of a file.

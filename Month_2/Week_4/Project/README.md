# Project - Library Management System

Build a small command-line library catalog. It combines dictionaries, validation, JSON persistence, modules, and tests. This is the Month 2 roadmap's Library Management System project.

The runnable reference implementation is [`library_management.py`](./library_management.py), with acceptance tests in [`test_library_management.py`](./test_library_management.py).

## Features

- Add books by unique ISBN with a title, author, and positive copy count
- Find and list books
- Check out an available copy and return a checked-out copy
- Save and load the catalog as JSON
- Report missing or invalid data rather than silently discarding it

## Run

From the repository root:

```bash
python -m Month_2.Week_4.Project.library_management
```

The first saved change creates `library_catalog.json` in the current working directory. To use another location, set the `LIBRARY_CATALOG` environment variable to its path. From this directory, run `python library_management.py`.

Run tests from the repository root:

```bash
python -m unittest -v Month_2.Week_4.Project.test_library_management
```

## Acceptance checklist

- [ ] ISBNs are unique and required fields cannot be blank.
- [ ] A checkout cannot reduce available copies below zero.
- [ ] A return cannot exceed the number of copies currently checked out.
- [ ] The catalog persists between runs and malformed JSON is reported.
- [ ] The tests pass.

## Extensions

- Add a borrower record and due date.
- Add search by title or author.
- Write the catalog to a temporary file before replacing the old file, to reduce the risk of a partial write.

# Week 3 - Files, modules, and packages

## Learning objectives

By the end of this week, you should be able to read and write text files safely, work with simple JSON data, distinguish common file errors, import reusable code from modules, and recognize a package structure.

## Seven-day plan

1. Paths, text encodings, and reading with `open()`
2. Write, append, and use `with` to close files reliably
3. Parse and write JSON with the `json` module
4. Handle expected file and decoding errors narrowly
5. Split reusable code into modules and import it
6. Explore a package and complete the [exercises](./Exercises/) and [quiz](./Quiz/Quiz.md)
7. Build the [File Analyzer](./Project/README.md)

## Core ideas

- Prefer `Path` from `pathlib` for filesystem paths. A relative path is interpreted from the process's current working directory.
- Use `with path.open(..., encoding="utf-8") as file:` so the file is closed even when an exception occurs.
- Use mode `"r"` to read, `"w"` to create or replace a file, and `"a"` to append. Avoid `"w"` when you mean to preserve existing contents.
- `read_text()` and `write_text()` are convenient for small files; specify an encoding.
- JSON represents a limited set of data types: objects, arrays, strings, numbers, booleans, and `null`. Python's `json` module maps these to dictionaries, lists, strings, numbers, booleans, and `None`.
- Catch expected failures such as `FileNotFoundError`, `OSError`, or `json.JSONDecodeError` at a layer that can respond meaningfully. Do not hide them with a broad empty-result fallback.
- A module is a `.py` file. A package groups modules in a directory; an `__init__.py` file can define its public imports. Use `if __name__ == "__main__":` to keep script execution separate from importing.

## Worked examples

- [Example 1: read a text file](./01_Examples.md)
- [Example 2: write and append safely](./02_Examples.md)
- [Example 3: read and write JSON](./03_Examples.md)
- [Example 4: modules and packages](./04_Examples.md)

## Project

Build and test the [File Analyzer](./Project/README.md). It reads a UTF-8 file and reports useful text statistics without changing the source file.

## Official references

- [Tutorial: Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Tutorial: Saving Structured Data with `json`](https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json)
- [Tutorial: Modules](https://docs.python.org/3/tutorial/modules.html)
- [Tutorial: Packages](https://docs.python.org/3/tutorial/modules.html#packages)
- [Tutorial: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Language Reference: The `with` statement](https://docs.python.org/3/reference/compound_stmts.html#with)
- [Language Reference: Import statements](https://docs.python.org/3/reference/simple_stmts.html#import)

## Checklist

- [ ] I can explain why a context manager is useful for a file.
- [ ] I can choose between `"r"`, `"w"`, and `"a"` without losing wanted data.
- [ ] I can save and load a list or dictionary as JSON.
- [ ] I can import a module without starting its command-line behavior.
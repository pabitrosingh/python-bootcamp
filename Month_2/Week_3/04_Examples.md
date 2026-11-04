# Week 3 / Example 4 - Modules and packages

Each Python file is a module. Put reusable definitions in a module, then import only the names a caller needs:

```python
# text_tools.py
def word_count(text):
    return len(text.split())
```

```python
# analyze.py
from text_tools import word_count

def main():
    print(word_count("Small modules are easier to reuse."))

if __name__ == "__main__":
    main()
```

When `analyze.py` is imported, `main()` is not called. This guard makes definitions importable without launching the script.

A package is a directory that groups related modules. A simple layout is:

```text
text_tools/
    __init__.py
    counts.py
    paths.py
```

For example, `text_tools/__init__.py` can expose `word_count` from `.counts`, and callers can use `from text_tools import word_count`. Run package code from its parent directory so Python can find the package. Avoid naming your files after standard-library modules such as `json.py` or `pathlib.py`.

**Try it:** Split a function you wrote into a module and import it into a second script. Confirm that importing it does not print output or prompt for input.
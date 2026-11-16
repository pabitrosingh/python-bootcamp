# Week 4 / Example 2 - A safe command-line interface

`argparse` defines inputs and generates help text. A destructive action can be opt-in:

```python
import argparse


def main():
    parser = argparse.ArgumentParser(description="Preview or apply a cleanup task.")
    parser.add_argument("directory")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="perform changes; without this flag, only preview them",
    )
    arguments = parser.parse_args()
    mode = "applying" if arguments.apply else "previewing"
    print(f"{mode} changes in {arguments.directory}")


if __name__ == "__main__":
    main()
```

**Try it:** Add a `--verbose` flag and use it to configure diagnostic logging.
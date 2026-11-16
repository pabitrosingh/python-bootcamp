# Project - Automation Suite: Safe File Organizer

Build a small command-line utility that groups files in one directory into subdirectories named for their extensions. The project practices `pathlib`, deterministic planning, logging, `argparse`, and testable filesystem operations.

The implementation is in [`organizer.py`](./organizer.py); tests are in [`test_organizer.py`](./test_organizer.py).

## Run

From the repository root:

```bash
python -m Month_5.Week_4.Project.organizer --help
python -m Month_5.Week_4.Project.organizer ./sample-files
python -m Month_5.Week_4.Project.organizer ./sample-files --apply
python -m unittest -v Month_5.Week_4.Project.test_organizer
```

The default command only previews moves. `--apply` is required to change files. The tool handles regular files directly inside the selected directory; it does not recurse into subdirectories or follow symbolic links. Test it on a temporary or disposable directory before using it on valuable data.

## Acceptance checklist

- [ ] Plan extension-based moves without changing the filesystem.
- [ ] Make dry-run the default and require an explicit `--apply`.
- [ ] Avoid overwriting an existing destination by selecting an unused name.
- [ ] Ignore directories and symbolic links in the source directory.
- [ ] Test preview, applying, collisions, and repeat runs with a temporary directory.

## Extensions

- Add a `--recursive` mode with a clear collision policy.
- Add an undo manifest that records completed moves.
- Add configurable rules from a JSON file.

## References

- [`pathlib`](https://docs.python.org/3/library/pathlib.html)
- [`argparse`](https://docs.python.org/3/library/argparse.html)
- [`logging`](https://docs.python.org/3/library/logging.html)
- [`shutil`](https://docs.python.org/3/library/shutil.html)

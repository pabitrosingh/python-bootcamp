# Project - Monitoring Tool: Directory Change Monitor

Build a polling monitor that detects files added, modified, or removed from one directory. The project practices immutable snapshots, generators, `pathlib`, `time.monotonic()`, and separation of detection logic from the command-line interface.

The implementation is in [`monitor.py`](./monitor.py); tests are in [`test_monitor.py`](./test_monitor.py).

## Run

From the repository root:

```bash
python -m Month_5.Week_2.Project.monitor --help
python -m Month_5.Week_2.Project.monitor ./logs --interval 2
python -m unittest -v Month_5.Week_2.Project.test_monitor
```

The monitor scans regular files recursively and reports their relative paths, sizes, and modification times. It does not read file contents or monitor changes outside the selected directory. Polling has a detection delay and can miss intermediate states between scans.

## Acceptance checklist

- [ ] Take a snapshot of file metadata without opening file contents.
- [ ] Report added, modified, and removed paths deterministically.
- [ ] Keep snapshot comparison separate from the long-running polling loop.
- [ ] Reject invalid intervals and missing/non-directory roots.
- [ ] Test snapshot comparison in a temporary directory without waiting for a real-time loop.

## Extensions

- Persist snapshots as JSON so monitoring can resume after a restart.
- Add a configurable ignore pattern.
- Add a health-check mode for a user-supplied HTTP endpoint with a timeout.
- Use a platform-specific filesystem notification library in a production version.

## References

- [`pathlib`](https://docs.python.org/3/library/pathlib.html)
- [`time.monotonic`](https://docs.python.org/3/library/time.html#time.monotonic)
- [`argparse`](https://docs.python.org/3/library/argparse.html)
- [`logging`](https://docs.python.org/3/library/logging.html)

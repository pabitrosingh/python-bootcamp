"""Poll a directory and report files added, modified, or removed."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import logging
from pathlib import Path
from time import monotonic, sleep
from typing import Iterator


logger = logging.getLogger(__name__)
Snapshot = dict[Path, tuple[int, int]]


@dataclass(frozen=True)
class DirectoryChanges:
    """Paths whose file metadata changed between two scans."""

    added: tuple[Path, ...]
    modified: tuple[Path, ...]
    removed: tuple[Path, ...]

    @property
    def has_changes(self) -> bool:
        return bool(self.added or self.modified or self.removed)


def scan_directory(root: str | Path) -> Snapshot:
    """Return relative file paths mapped to (size, modification time in ns)."""
    directory = Path(root)
    if not directory.exists():
        raise FileNotFoundError(directory)
    if not directory.is_dir():
        raise NotADirectoryError(directory)

    snapshot: Snapshot = {}
    for path in directory.rglob("*"):
        if path.is_symlink() or not path.is_file():
            continue
        stat = path.stat()
        snapshot[path.relative_to(directory)] = (stat.st_size, stat.st_mtime_ns)
    return snapshot


def compare_snapshots(previous: Snapshot, current: Snapshot) -> DirectoryChanges:
    """Return sorted added, modified, and removed paths."""
    previous_paths = previous.keys()
    current_paths = current.keys()
    added = tuple(sorted(current_paths - previous_paths))
    removed = tuple(sorted(previous_paths - current_paths))
    modified = tuple(
        sorted(
            path
            for path in previous_paths & current_paths
            if previous[path] != current[path]
        )
    )
    return DirectoryChanges(added, modified, removed)


def watch_directory(
    root: str | Path, interval: float = 1.0
) -> Iterator[DirectoryChanges]:
    """Yield non-empty changes found by periodic directory scans."""
    if interval <= 0:
        raise ValueError("interval must be positive")
    previous = scan_directory(root)
    while True:
        next_scan = monotonic() + interval
        sleep(max(0.0, next_scan - monotonic()))
        current = scan_directory(root)
        changes = compare_snapshots(previous, current)
        if changes.has_changes:
            yield changes
        previous = current


def _log_changes(changes: DirectoryChanges) -> None:
    for label, paths in (
        ("Added", changes.added),
        ("Modified", changes.modified),
        ("Removed", changes.removed),
    ):
        for path in paths:
            logger.info("%s: %s", label, path)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="directory to monitor")
    parser.add_argument("--interval", type=float, default=1.0, help="seconds between scans")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(asctime)s %(levelname)s: %(message)s",
    )

    try:
        for changes in watch_directory(args.directory, args.interval):
            _log_changes(changes)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    except KeyboardInterrupt:
        logger.info("Monitoring stopped")


if __name__ == "__main__":
    main()

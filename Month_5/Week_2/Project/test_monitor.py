import tempfile
import unittest
from pathlib import Path

from Month_5.Week_2.Project.monitor import (
    DirectoryChanges,
    compare_snapshots,
    scan_directory,
    watch_directory,
)


class MonitorTests(unittest.TestCase):
    def test_compare_snapshots_classifies_all_change_types(self):
        previous = {
            Path("same.txt"): (3, 10),
            Path("changed.txt"): (1, 10),
            Path("removed.txt"): (5, 10),
        }
        current = {
            Path("same.txt"): (3, 10),
            Path("changed.txt"): (2, 11),
            Path("added.txt"): (4, 12),
        }

        changes = compare_snapshots(previous, current)

        self.assertEqual(
            changes,
            DirectoryChanges(
                added=(Path("added.txt"),),
                modified=(Path("changed.txt"),),
                removed=(Path("removed.txt"),),
            ),
        )
        self.assertTrue(changes.has_changes)

    def test_scan_directory_returns_relative_file_metadata(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            nested = root / "nested"
            nested.mkdir()
            file_path = nested / "data.txt"
            file_path.write_text("hello", encoding="utf-8")

            snapshot = scan_directory(root)

            self.assertEqual(snapshot.keys(), {Path("nested/data.txt")})
            self.assertEqual(snapshot[Path("nested/data.txt")][0], 5)

    def test_scan_directory_rejects_missing_root(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            missing = Path(temporary_directory) / "missing"
            with self.assertRaises(FileNotFoundError):
                scan_directory(missing)

    def test_watch_directory_rejects_non_positive_interval(self):
        with self.assertRaises(ValueError):
            next(watch_directory(".", interval=0))

    def test_empty_snapshot_diff_has_no_changes(self):
        self.assertFalse(compare_snapshots({}, {}).has_changes)


if __name__ == "__main__":
    unittest.main()

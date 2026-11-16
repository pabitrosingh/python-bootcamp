import tempfile
import unittest
from pathlib import Path

from Month_5.Week_4.Project.organizer import (
    Move,
    apply_moves,
    plan_organization,
)


class OrganizerTests(unittest.TestCase):
    def test_planning_does_not_change_filesystem(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            report = root / "report.PDF"
            report.write_text("data", encoding="utf-8")

            moves = plan_organization(root)

            self.assertEqual(moves, (Move(report, root / "pdf" / "report.PDF"),))
            self.assertTrue(report.exists())
            self.assertFalse((root / "pdf").exists())

    def test_apply_moves_files_and_repeat_plan_is_empty(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "notes.txt").write_text("notes", encoding="utf-8")
            (root / "README").write_text("readme", encoding="utf-8")

            completed = apply_moves(plan_organization(root))

            self.assertEqual(len(completed), 2)
            self.assertEqual((root / "txt" / "notes.txt").read_text(), "notes")
            self.assertEqual(
                (root / "no_extension" / "README").read_text(), "readme"
            )
            self.assertEqual(plan_organization(root), ())

    def test_collision_uses_an_unused_name(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            destination = root / "txt"
            destination.mkdir()
            (destination / "report.txt").write_text("old", encoding="utf-8")
            (root / "report.txt").write_text("new", encoding="utf-8")

            moves = plan_organization(root)
            self.assertEqual(moves[0].destination, destination / "report_1.txt")
            apply_moves(moves)

            self.assertEqual(
                (destination / "report.txt").read_text(encoding="utf-8"), "old"
            )
            self.assertEqual(
                (destination / "report_1.txt").read_text(encoding="utf-8"), "new"
            )

    def test_ignores_directories_and_symlinks(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "subdir").mkdir()
            target = root / "target.txt"
            target.write_text("target", encoding="utf-8")
            link = root / "link.txt"
            try:
                link.symlink_to(target)
            except (NotImplementedError, OSError):
                self.skipTest("symbolic links are not available")

            self.assertEqual(plan_organization(root), (Move(target, root / "txt" / "target.txt"),))

    def test_missing_directory_fails_explicitly(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            missing = Path(temporary_directory) / "missing"
            with self.assertRaises(FileNotFoundError):
                plan_organization(missing)


if __name__ == "__main__":
    unittest.main()

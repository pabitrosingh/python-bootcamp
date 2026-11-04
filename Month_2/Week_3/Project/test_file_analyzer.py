import tempfile
import unittest
from pathlib import Path

from Month_2.Week_3.Project.file_analyzer import analyze_file, analyze_text


class FileAnalyzerTests(unittest.TestCase):
    def test_analyze_text_counts_characters_lines_words_and_frequency(self):
        report = analyze_text("Hello, hello!\nPython's fun.")
        self.assertEqual(report["character_count"], 27)
        self.assertEqual(report["line_count"], 2)
        self.assertEqual(report["word_count"], 4)
        self.assertEqual(report["top_words"], [("hello", 2), ("fun", 1), ("python's", 1)])

    def test_empty_and_whitespace_text(self):
        self.assertEqual(
            analyze_text(""),
            {"character_count": 0, "line_count": 0, "word_count": 0, "top_words": []},
        )
        report = analyze_text(" \n\t")
        self.assertEqual(report["character_count"], 3)
        self.assertEqual(report["line_count"], 2)
        self.assertEqual(report["word_count"], 0)

    def test_top_words_are_deterministic_for_ties(self):
        self.assertEqual(analyze_text("pear apple", top_n=2)["top_words"], [("apple", 1), ("pear", 1)])

    def test_negative_top_count_is_rejected(self):
        with self.assertRaises(ValueError):
            analyze_text("words", top_n=-1)

    def test_analyze_file_reads_utf8_without_changing_content(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "notes.txt"
            original = "café\n"
            path.write_text(original, encoding="utf-8")
            report = analyze_file(path)
            self.assertEqual(report["character_count"], len(original))
            self.assertEqual(path.read_text(encoding="utf-8"), original)

    def test_analyze_file_raises_for_missing_path(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "missing.txt"
            with self.assertRaises(FileNotFoundError):
                analyze_file(path)


if __name__ == "__main__":
    unittest.main()

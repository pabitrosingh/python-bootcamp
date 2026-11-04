import json
import tempfile
import unittest
from pathlib import Path

from Month_2.Week_4.Project.library_management import (
    add_book,
    checkout_book,
    find_book,
    list_books,
    load_catalog,
    return_book,
    save_catalog,
)


class LibraryManagementTests(unittest.TestCase):
    def setUp(self):
        self.catalog = {}
        add_book(self.catalog, " 001 ", "Python Basics", "A. Writer", 2)

    def test_add_book_normalizes_text_and_rejects_invalid_values(self):
        book = self.catalog["001"]
        self.assertEqual(book["isbn"], "001")
        self.assertEqual(book["available_copies"], 2)
        for isbn, title, author, copies in [
            ("002", "", "Author", 1),
            ("001", "Duplicate", "Author", 1),
            ("003", "Title", "Author", 0),
            ("004", "Title", "Author", 1.5),
        ]:
            with self.subTest(isbn=isbn, title=title, copies=copies):
                with self.assertRaises(ValueError):
                    add_book(self.catalog, isbn, title, author, copies)
        self.assertEqual(len(self.catalog), 1)

    def test_checkout_and_return_enforce_copy_limits(self):
        checkout_book(self.catalog, "001")
        checkout_book(self.catalog, "001")
        self.assertEqual(self.catalog["001"]["available_copies"], 0)
        with self.assertRaises(ValueError):
            checkout_book(self.catalog, "001")
        return_book(self.catalog, "001")
        self.assertEqual(self.catalog["001"]["available_copies"], 1)
        return_book(self.catalog, "001")
        self.assertEqual(self.catalog["001"]["available_copies"], 2)
        with self.assertRaises(ValueError):
            return_book(self.catalog, "001")

    def test_missing_isbn_raises_key_error(self):
        self.assertIsNone(find_book(self.catalog, "missing"))
        with self.assertRaises(KeyError):
            checkout_book(self.catalog, "missing")

    def test_list_books_is_sorted_by_title(self):
        add_book(self.catalog, "002", "A Different Book", "B. Writer", 1)
        self.assertEqual([book["isbn"] for book in list_books(self.catalog)], ["002", "001"])

    def test_save_and_load_round_trip(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "catalog.json"
            checkout_book(self.catalog, "001")
            checkout_book(self.catalog, "001")
            save_catalog(self.catalog, path)
            self.assertEqual(load_catalog(path), self.catalog)

    def test_load_rejects_malformed_and_invalid_catalogs(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "catalog.json"
            path.write_text("{", encoding="utf-8")
            with self.assertRaises(json.JSONDecodeError):
                load_catalog(path)
            path.write_text(json.dumps({"001": {"isbn": "001", "title": "Bad"}}), encoding="utf-8")
            with self.assertRaises(ValueError):
                load_catalog(path)


if __name__ == "__main__":
    unittest.main()

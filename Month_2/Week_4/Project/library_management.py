"""Command-line library catalog with JSON persistence."""

import json
import os
import sys
from pathlib import Path


def add_book(catalog, isbn, title, author, total_copies):
    isbn = isbn.strip()
    title = title.strip()
    author = author.strip()
    if not isbn or not title or not author:
        raise ValueError("ISBN, title, and author cannot be blank.")
    if isbn in catalog:
        raise ValueError(f"ISBN {isbn!r} already exists.")
    if isinstance(total_copies, bool) or not isinstance(total_copies, int) or total_copies < 1:
        raise ValueError("Total copies must be a positive whole number.")

    book = {
        "isbn": isbn,
        "title": title,
        "author": author,
        "total_copies": total_copies,
        "available_copies": total_copies,
    }
    catalog[isbn] = book
    return book


def find_book(catalog, isbn):
    return catalog.get(isbn.strip())


def checkout_book(catalog, isbn):
    book = find_book(catalog, isbn)
    if book is None:
        raise KeyError(f"No book with ISBN {isbn.strip()!r}.")
    if book["available_copies"] == 0:
        raise ValueError(f"No copies of {book['title']!r} are available.")
    book["available_copies"] -= 1
    return book


def return_book(catalog, isbn):
    book = find_book(catalog, isbn)
    if book is None:
        raise KeyError(f"No book with ISBN {isbn.strip()!r}.")
    if book["available_copies"] == book["total_copies"]:
        raise ValueError(f"No copy of {book['title']!r} is checked out.")
    book["available_copies"] += 1
    return book


def list_books(catalog):
    return sorted(catalog.values(), key=lambda book: (book["title"].casefold(), book["isbn"]))


def save_catalog(catalog, path):
    destination = Path(path)
    destination.write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _validate_catalog(data):
    if not isinstance(data, dict):
        raise ValueError("Catalog JSON must contain an object keyed by ISBN.")

    for isbn, book in data.items():
        if not isinstance(isbn, str) or not isbn.strip() or not isinstance(book, dict):
            raise ValueError("Each catalog entry must map an ISBN string to a book object.")
        if book.get("isbn") != isbn:
            raise ValueError(f"Catalog key does not match book ISBN {isbn!r}.")
        if not all(isinstance(book.get(field), str) and book[field].strip() for field in ("title", "author")):
            raise ValueError(f"Book {isbn!r} must have a non-blank title and author.")
        total = book.get("total_copies")
        available = book.get("available_copies")
        if (
            isinstance(total, bool)
            or not isinstance(total, int)
            or isinstance(available, bool)
            or not isinstance(available, int)
            or not 1 <= total
            or not 0 <= available <= total
        ):
            raise ValueError(f"Book {isbn!r} has invalid copy counts.")
    return data


def load_catalog(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return _validate_catalog(data)


def main():
    catalog_path = Path(os.environ.get("LIBRARY_CATALOG", "library_catalog.json"))
    try:
        catalog = load_catalog(catalog_path) if catalog_path.exists() else {}
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError) as error:
        print(f"Could not load catalog {catalog_path}: {error}", file=sys.stderr)
        return 1

    if not catalog_path.exists():
        print(f"Starting a new catalog at {catalog_path}.")

    try:
        while True:
            print("\nLibrary Management System")
            print("1. Add book  2. Find book  3. List books")
            print("4. Check out  5. Return  6. Quit")
            choice = input("Choose an option: ").strip()
            try:
                if choice == "1":
                    book = add_book(
                        catalog,
                        input("ISBN: "),
                        input("Title: "),
                        input("Author: "),
                        int(input("Total copies: ").strip()),
                    )
                    save_catalog(catalog, catalog_path)
                    print(f"Added {book['title']}.")
                elif choice == "2":
                    book = find_book(catalog, input("ISBN: "))
                    print(book if book is not None else "Book not found.")
                elif choice == "3":
                    for book in list_books(catalog):
                        print(
                            f"{book['isbn']} | {book['title']} by {book['author']} "
                            f"| {book['available_copies']}/{book['total_copies']} available"
                        )
                elif choice == "4":
                    book = checkout_book(catalog, input("ISBN: "))
                    save_catalog(catalog, catalog_path)
                    print(f"Checked out {book['title']}.")
                elif choice == "5":
                    book = return_book(catalog, input("ISBN: "))
                    save_catalog(catalog, catalog_path)
                    print(f"Returned {book['title']}.")
                elif choice == "6":
                    print("Goodbye.")
                    return 0
                else:
                    print("Choose a number from 1 to 6.")
            except (ValueError, KeyError) as error:
                print(f"Catalog not changed: {error}")
    except (OSError, UnicodeDecodeError) as error:
        print(f"Could not save catalog {catalog_path}: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

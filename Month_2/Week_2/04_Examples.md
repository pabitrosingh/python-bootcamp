# Week 2 / Example 4 - Nested records and safe access

A list of dictionaries is useful for a collection of similar records:

```python
contacts = [
    {"name": "Ada", "email": "ada@example.com"},
    {"name": "Grace", "email": "grace@example.com"},
]

for contact in contacts:
    print(f"{contact['name']}: {contact.get('email', 'no email')}")
```

A dictionary keyed by an identifier can make lookup direct:

```python
books = {
    "9780000000001": {"title": "A Sample Book", "available": True},
}
isbn = "9780000000001"
book = books.get(isbn)
if book is not None:
    print(book["title"])
```

Choose the outer structure based on the operation you need most often. For example, a dictionary keyed by normalized contact name supports fast name lookup; a list is convenient when preserving entry order and duplicates matters.

**Try it:** Add a third contact, then print all names alphabetically without changing the original list.
# Project - Contact Manager

Build a command-line contact manager using a dictionary for unique, normalized name lookup. This is the Month 2 roadmap's Contact Manager project.

The runnable reference implementation is [`contact_manager.py`](./contact_manager.py), with acceptance tests in [`test_contact_manager.py`](./test_contact_manager.py).

## Features

- Add a contact with a name and at least one email or phone number
- Find, update, and delete a contact by name (case-insensitive)
- List contacts alphabetically
- Reject blank names, duplicate names, and updates to missing contacts
- Keep the data in memory for this project; persistence is covered in Week 3

## Run

From the repository root:

```bash
python -m Month_2.Week_2.Project.contact_manager
```

Or from this directory:

```bash
python contact_manager.py
```

Run the automated tests from the repository root:

```bash
python -m unittest -v Month_2.Week_2.Project.test_contact_manager
```

## Acceptance checklist

- [ ] Names differing only in capitalization cannot create duplicate contacts.
- [ ] Invalid additions and updates leave existing data unchanged.
- [ ] Missing contacts can be reported without an uncaught `KeyError`.
- [ ] Listing contacts is alphabetical and does not mutate the stored mapping.
- [ ] The tests pass.

## Extensions

- Add a search by email or phone number.
- Save and load contacts as JSON after completing Week 3.
- Add input validation in the CLI for menu choices.

import unittest

from Month_2.Week_2.Project.contact_manager import (
    add_contact,
    delete_contact,
    find_contact,
    list_contacts,
    update_contact,
)


class ContactManagerTests(unittest.TestCase):
    def test_add_and_find_normalizes_name_for_lookup(self):
        contacts = {}
        contact = add_contact(contacts, " Ada ", " ada@example.com ")
        self.assertEqual(contact["name"], "Ada")
        self.assertIs(find_contact(contacts, "ADA"), contact)

    def test_add_rejects_blank_name_or_missing_contact_method(self):
        for name, email, phone in [
            (" ", "ada@example.com", ""),
            ("Ada", "", ""),
        ]:
            with self.subTest(name=name, email=email, phone=phone):
                with self.assertRaises(ValueError):
                    add_contact({}, name, email, phone)

    def test_add_rejects_duplicate_case_insensitive_name(self):
        contacts = {}
        add_contact(contacts, "Ada", phone="555-0100")
        with self.assertRaises(ValueError):
            add_contact(contacts, " ada ", email="other@example.com")
        self.assertEqual(len(contacts), 1)

    def test_update_changes_fields_and_rejects_empty_contact(self):
        contacts = {}
        add_contact(contacts, "Ada", email="ada@example.com", phone="555-0100")
        updated = update_contact(contacts, "Ada", email="new@example.com")
        self.assertEqual(updated["email"], "new@example.com")
        self.assertEqual(updated["phone"], "555-0100")
        with self.assertRaises(ValueError):
            update_contact(contacts, "Ada", email="", phone="")
        self.assertEqual(updated["email"], "new@example.com")

    def test_update_missing_contact_raises_key_error(self):
        with self.assertRaises(KeyError):
            update_contact({}, "missing", phone="555-0100")

    def test_delete_is_safe_and_list_is_sorted(self):
        contacts = {}
        add_contact(contacts, "Zoe", phone="555-0100")
        add_contact(contacts, "Ada", phone="555-0101")
        self.assertEqual([item["name"] for item in list_contacts(contacts)], ["Ada", "Zoe"])
        self.assertTrue(delete_contact(contacts, "ZOE"))
        self.assertFalse(delete_contact(contacts, "Zoe"))


if __name__ == "__main__":
    unittest.main()

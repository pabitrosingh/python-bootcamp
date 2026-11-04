"""In-memory command-line contact manager."""


def _contact_key(name):
    return name.strip().casefold()


def add_contact(contacts, name, email="", phone=""):
    name = name.strip()
    email = email.strip()
    phone = phone.strip()
    key = _contact_key(name)

    if not name:
        raise ValueError("Contact name cannot be blank.")
    if not email and not phone:
        raise ValueError("Provide an email address, a phone number, or both.")
    if key in contacts:
        raise ValueError(f"A contact named {name!r} already exists.")

    contact = {"name": name, "email": email, "phone": phone}
    contacts[key] = contact
    return contact


def find_contact(contacts, name):
    return contacts.get(_contact_key(name))


def update_contact(contacts, name, email=None, phone=None):
    contact = find_contact(contacts, name)
    if contact is None:
        raise KeyError(f"No contact named {name.strip()!r}.")

    new_email = contact["email"] if email is None else email.strip()
    new_phone = contact["phone"] if phone is None else phone.strip()
    if not new_email and not new_phone:
        raise ValueError("A contact must have an email address or phone number.")

    contact["email"] = new_email
    contact["phone"] = new_phone
    return contact


def delete_contact(contacts, name):
    return contacts.pop(_contact_key(name), None) is not None


def list_contacts(contacts):
    return sorted(contacts.values(), key=lambda contact: contact["name"].casefold())


def main():
    contacts = {}
    while True:
        print("\nContact Manager")
        print("1. Add  2. Find  3. Update  4. Delete  5. List  6. Quit")
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                contact = add_contact(
                    contacts,
                    input("Name: "),
                    input("Email (optional): "),
                    input("Phone (optional): "),
                )
                print(f"Added {contact['name']}.")
            elif choice == "2":
                contact = find_contact(contacts, input("Name: "))
                print(contact if contact is not None else "Contact not found.")
            elif choice == "3":
                name = input("Name: ")
                email = input("New email (blank to keep current): ")
                phone = input("New phone (blank to keep current): ")
                contact = find_contact(contacts, name)
                if contact is None:
                    raise KeyError(f"No contact named {name.strip()!r}.")
                update_contact(
                    contacts,
                    name,
                    email=email or None,
                    phone=phone or None,
                )
                print(f"Updated {contact['name']}.")
            elif choice == "4":
                name = input("Name: ")
                print("Deleted." if delete_contact(contacts, name) else "Contact not found.")
            elif choice == "5":
                for contact in list_contacts(contacts):
                    print(contact)
            elif choice == "6":
                print("Goodbye.")
                return
            else:
                print("Choose a number from 1 to 6.")
        except (ValueError, KeyError) as error:
            print(f"Contact not changed: {error}")


if __name__ == "__main__":
    main()

import json
import os

class ContactNotFoundError(Exception):
    pass

FILENAME = "contacts.json"

def load_contacts():
    if not os.path.exists(FILENAME):
        return {}
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Contacts file corrupted, starting fresh.")
        return {}


def save_contacts(contacts):
    with open(FILENAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(name, phone):
    contacts = load_contacts()
    contacts[name] = phone
    save_contacts(contacts)
    print(f"Added: {name} - {phone}")


def get_contact(name):
    contacts = load_contacts()
    if name not in contacts:
        raise ContactNotFoundError(f"No contact found for '{name}'")
    return contacts[name]


def delete_contact(name):
    contacts = load_contacts()
    if name not in contacts:
        raise ContactNotFoundError(f"No contact found for '{name}'")
    del contacts[name]
    save_contacts(contacts)
    print(f"Deleted: {name}")


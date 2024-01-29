import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=2)

def add_contact(name, phone, email):
    contacts = load_contacts()
    new_contact = {"name": name, "phone": phone, "email": email}
    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

def search_contact(name):
    contacts = load_contacts()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print_contact(contact)
            return
    print(f"No contact found with the name '{name}'.")

def update_contact(name, phone, email):
    contacts = load_contacts()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = phone
            contact["email"] = email
            save_contacts(contacts)
            print(f"Contact '{name}' updated successfully.")
            return
    print(f"No contact found with the name '{name}'.")

def print_contact(contact):
    print("Name:", contact["name"])
    print("Phone:", contact["phone"])
    print("Email:", contact["email"])
    print()

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            if len(phone)==10:
                add_contact(name, phone, email)
                break
            else:
                print("add a 10 digit number")

        elif choice == '2':
            name = input("Enter the name to search: ")
            search_contact(name)

        elif choice == '3':
            name = input("Enter the name to update: ")
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email address: ")
            update_contact(name, phone, email)

        elif choice == '4':
            print("Exiting the Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

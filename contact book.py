# Contact list Management System

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def update(self, phone=None, email=None, address=None):
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}\n"


class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        if name in self.contacts:
            print("Contact already exists!")
        else:
            self.contacts[name] = Contact(name, phone, email, address)
            print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for name, contact in self.contacts.items():
                print(contact)
                print('-' * 20)

    def search_contact(self, query):
        found = False
        for name, contact in self.contacts.items():
            if query.lower() in name.lower() or query in contact.phone:
                print(contact)
                print('-' * 20)
                found = True
        if not found:
            print("No matching contact found.")

    def update_contact(self, name, phone=None, email=None, address=None):
        if name in self.contacts:
            self.contacts[name].update(phone, email, address)
            print(f"Contact {name} updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print("Contact not found.")

    def run(self):
        while True:
            print("\n--- Contact Management ---")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = input("Choose an option: ")
            
            if choice == '1':
                name = input("Enter Store Name: ")
                phone = input("Enter Phone Number: ")
                email = input("Enter Email: ")
                address = input("Enter Address: ")
                self.add_contact(name, phone, email, address)
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                query = input("Enter name or phone number to search: ")
                self.search_contact(query)
            elif choice == '4':
                name = input("Enter the name of the contact to update: ")
                phone = input("Enter new Phone Number (leave blank to skip): ")
                email = input("Enter new Email (leave blank to skip): ")
                address = input("Enter new Address (leave blank to skip): ")
                self.update_contact(name, phone or None, email or None, address or None)
            elif choice == '5':
                name = input("Enter the name of the contact to delete: ")
                self.delete_contact(name)
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid option! Please try again.")


if __name__ == "__main__":
    manager = ContactManager()
    manager.run()

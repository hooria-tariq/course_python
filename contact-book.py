def display_menu():
    print("\nContact Book Menu:")
    print("1. Add a new contact")
    print("2. Search for a contact")
    print("3. Delete a contact")
    print("4. View all contacts")
    print("5. Exit")

def add_contact(contacts):
    name = input("Enter contact name: ")
    if name in contacts:
        print(f"{name} already exists in contacts!")
        return
    
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"Contact '{name}' added successfully!")

def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"Contact '{name}' not found!")

def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found!")

def view_contacts(contacts):
    if not contacts:
        print("Your contact book is empty!")
        return
    
    print("\nAll Contacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def contact_book():
    contacts = {}
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            view_contacts(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-5.")

contact_book()
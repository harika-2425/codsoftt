contacts = []

def add_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")

    contact = {
        'Name': name,
        'Phone Number': phone_number,
        'Email': email,
        'Address': address
    }

    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contact_list():
    print("\nName\t\t\tPhone Number\t\tEmail\t\t\tAddress\n")
    for contact in contacts:
        print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(contact['Name'], contact['Phone Number'], contact['Email'], contact['Address']))
    print()

def search_contact():
    search_term = input("\nEnter search term (Name or Phone Number): ")
    search_results = []

    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone Number']:
            search_results.append(contact)

    if search_results:
        print("\nSearch result:")
        for result in search_results:
            print("Name: {}, Phone Number: {}, Email: {}, Address: {}".format(result['Name'], result['Phone Number'], result['Email'], result['Address']))
    else:
        print("Contact Not Found")

def update_contact():
    search_term = input("\nEnter the name of the contact to update: ")
    for contact in contacts:
        if search_term.lower() == contact['Name'].lower():
            print("\nCurrent Details:")
            print("Name: {}, Phone Number: {}, Email: {}, Address: {}".format(contact['Name'], contact['Phone Number'], contact['Email'], contact['Address']))

            contact['Phone Number'] = input("Enter new phone number: ")
            contact['Email'] = input("Enter new email: ")
            contact['Address'] = input("Enter new address: ")

            print("Contact updated successfully!\n")
            return

    print("Contact Not Found")

def delete_contact():
    search_term = input("\nEnter the name of the contact to delete: ")
    for contact in contacts:
        if search_term.lower() == contact['Name'].lower():
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return

    print("Contact Not Found")

def main():
    while True:
        print("\n*** Contact Management System ***")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

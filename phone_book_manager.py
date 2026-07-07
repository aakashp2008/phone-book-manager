def add_contact():
    name = input("Enter Name: ")
    number = input("Enter Phone Number: ")

    file = open("contacts.txt", "a")
    file.write(name + " - " + number + "\n")
    file.close()

    print("Contact added successfully!")

def view_contacts():
    try:
        file = open("contacts.txt", "r")
        print("\n=== Contact List ===")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("No contacts found.")

def search_contact():
    search = input("Enter contact name: ")

    try:
        file = open("contacts.txt", "r")
        found = False

        for line in file:
            if search.lower() in line.lower():
                print("Contact Found:", line)
                found = True

        if not found:
            print("Contact not found.")

        file.close()

    except FileNotFoundError:
        print("No contacts found.")

while True:
    print("\n=== Phone Book Manager ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        print("Thank you for using Phone Book Manager!")
        break

    else:
        print("Invalid choice.")

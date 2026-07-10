# Alejandro Valentin
# R-GLAB 385.3.1 Contact List Application data saved in File
# Date: July 2026

# Contact List Application
# Write contact to the file
# do not forget to add a file path

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    with open("contacts.txt", "a") as file:
        file.write(f"{name}: {phone}\n")
    print(f"\n{name} has been added to your contacts!")
# ====================================
# TEST BLOCK Comment out once verified
# ====================================
# if __name__ == "__main__":
#     add_contact()
# ====================================

# after testing the view_contacts function, I found that I was missing an 's' in contacts.txt
def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("\nYour contact list is empty.")
            else:
                print("\nYour contact list:")
                for contact in contacts:
                    print(contact, end='')
    except FileNotFoundError:
        print("\nYour contact list is empty.")
# ====================================
# TEST BLOCK Comment out once verified
# ====================================
# if __name__ == "__main__":
#     view_contacts()
# ====================================

def del_contact():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
        
        if not contacts:
            print("\nYour Contact list is empty.")
            return

        # Show contacts with numbers for selection
        print("\nYour contact list: \n")
        for i, contact in enumerate(contacts, 1):
            print(f"\n{i}. {contact.strip()}")

        # Get selection
        choice = int(input("\nEnter the number of the contact to delete: "))
        
        if 1 <= choice <= len(contacts):
            removed = contacts.pop(choice - 1)
            # Write the updated list back to the file
            with open("contacts.txt", "w") as file:
                file.writelines(contacts)
            print(f"\nSuccess: '{removed.strip()}' has been deleted.")
        else:
            print("\nInvalid selection.")

    except FileNotFoundError:
        print("\nYour contact list is empty (file not found).")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")

def main():
    while True:
        print("\nContact List Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Quit")
        choice = input("\nEnter your choice: " )
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            del_contact()
        elif choice == "4":
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice. Please try again.")
if __name__ == "__main__":
    main()

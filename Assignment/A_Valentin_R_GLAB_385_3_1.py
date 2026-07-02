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
    print(f"{name} has been added to your contacts!")
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
                print("Your contact list is empty.")
            else:
                print("Your contact list:")
                for contact in contacts:
                    print(contact, end='')
    except FileNotFoundError:
        print("Your contact list is empty.")
# ====================================
# TEST BLOCK Comment out once verified
# ====================================
# if __name__ == "__main__":
#     view_contacts()
# ====================================

def main():
    while True:
        print("\nContact List Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Quit")
        choice = input("Enter your choice: " )
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
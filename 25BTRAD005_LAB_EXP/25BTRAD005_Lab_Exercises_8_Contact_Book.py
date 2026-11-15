# ============================================================
# Lab Exercise 8: Contact Book using Lists and Dictionaries
# Name   : Adhithi Vagmye
# USN    : 25BTRAD005
# ============================================================

contacts = []

def find_contact(name):
    for c in contacts:
        if c["name"].lower() == name.lower():
            return c
    return None

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    if not (phone.isdigit() and len(phone) == 10):
        print("Invalid phone number. Contact not added.")
        return
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added.")

def search_contact():
    c = find_contact(input("Enter name to search: "))
    if c:
        print("Found:", c["name"], "|", c["phone"], "|", c["email"])
    else:
        print("Contact not found.")

def update_contact():
    c = find_contact(input("Enter name to update: "))
    if c:
        c["phone"] = input("Enter new phone: ")
        c["email"] = input("Enter new email: ")
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    c = find_contact(input("Enter name to delete: "))
    if c:
        contacts.remove(c)
        print("Contact deleted.")
    else:
        print("Contact not found.")

def display_contacts():
    if not contacts:
        print("Contact book is empty.")
        return
    print(f"{'Name':<8}{'Phone':<12}{'Email'}")
    for c in contacts:
        print(f"{c['name']:<8}{c['phone']:<12}{c['email']}")

while True:
    print("1.Add 2.Search 3.Update 4.Delete 5.Display 6.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice.")

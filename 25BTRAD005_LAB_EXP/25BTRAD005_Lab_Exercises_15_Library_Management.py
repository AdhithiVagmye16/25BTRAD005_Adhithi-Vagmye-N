# ============================================================
# Lab Exercise 15: Library Management System (Inheritance)
# Name   : Adhithi Vagmye
# USN    : 25BTRAD005
# ============================================================

class LibraryItem:
    def __init__(self, title):
        self.title = title
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            return True
        return False

    def give_back(self):
        if not self.available:
            self.available = True
            return True
        return False

    def details(self):
        status = "Available" if self.available else "Issued"
        return f"{self.title:<20}{status:<11}"


class Book(LibraryItem):                      # inheritance
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def details(self):
        return super().details() + f"Book by {self.author}"


class Magazine(LibraryItem):                  # inheritance
    def __init__(self, title, issue_no):
        super().__init__(title)
        self.issue_no = issue_no

    def details(self):
        return super().details() + f"Magazine, Issue {self.issue_no}"


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def find(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                return item
        return None

    def display(self):
        print(f"{'Title':<20}{'Status':<11}Type")
        for item in self.items:
            print(item.details())

    def issue_item(self, title):
        item = self.find(title)
        if item is None:
            print("Item not found.")
        elif item.issue():
            print(f"'{item.title}' issued successfully.")
        else:
            print(f"'{item.title}' is already issued.")

    def return_item(self, title):
        item = self.find(title)
        if item is None:
            print("Item not found.")
        elif item.give_back():
            print(f"'{item.title}' returned successfully.")
        else:
            print(f"'{item.title}' was not issued.")


lib = Library()
lib.add_item(Book("Python Basics", "Guido Rossum"))
lib.add_item(Book("Data Structures", "Mark Allen"))
lib.add_item(Magazine("Tech Today", 42))

while True:
    print("\n1.Display 2.Issue 3.Return 4.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        lib.display()
    elif choice == "2":
        lib.issue_item(input("Enter title to issue: "))
    elif choice == "3":
        lib.return_item(input("Enter title to return: "))
    elif choice == "4":
        print("Exiting Library System.")
        break
    else:
        print("Invalid choice.")

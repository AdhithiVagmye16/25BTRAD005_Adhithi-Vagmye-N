# ============================================================
# Lab Exercise 12: Student Data Manager using Files
# Name   : Adhithi Vagmye
# USN    : 25BTRAD005
# ============================================================

FILE = "students.txt"

def read_records():
    records = []
    try:
        with open(FILE, "r") as f:
            for line in f:
                if line.strip():
                    records.append(line.strip().split(","))
    except FileNotFoundError:
        pass
    return records

def write_records(records):
    with open(FILE, "w") as f:
        for r in records:
            f.write(",".join(r) + "\n")

def add_student():
    roll = input("Enter roll no: ")
    if any(r[0] == roll for r in read_records()):
        print("Roll number already exists.")
        return
    name = input("Enter name: ")
    marks = input("Enter marks (0-100): ")
    if not marks.isdigit() or int(marks) > 100:
        print("Invalid marks. Record not added.")
        return
    with open(FILE, "a") as f:
        f.write(f"{roll},{name},{marks}\n")
    print("Record added.")

def display_students():
    records = read_records()
    if not records:
        print("No records found.")
        return
    print(f"{'Roll':<7}{'Name':<10}{'Marks'}")
    for r in records:
        print(f"{r[0]:<7}{r[1]:<10}{r[2]}")

def search_student():
    roll = input("Enter roll no to search: ")
    for r in read_records():
        if r[0] == roll:
            print("Found:", r[1], "- Marks:", r[2])
            return
    print("Record not found.")

def update_student():
    roll = input("Enter roll no to update: ")
    records = read_records()
    for r in records:
        if r[0] == roll:
            r[2] = input("Enter new marks: ")
            write_records(records)
            print("Record updated.")
            return
    print("Record not found.")

while True:
    print("1.Add 2.Display 3.Search 4.Update 5.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        print("Exiting Student Data Manager.")
        break
    else:
        print("Invalid choice.")

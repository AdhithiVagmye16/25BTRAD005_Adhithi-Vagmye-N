# ============================================================
# Mini Project (Unit 3): Attendance Tracker
# Name   : Adhithi Vagmye
# USN    : 25BTRAD005
# ============================================================
# Concepts used: lists, dictionaries, functions, loops, conditionals, string formatting

students = {}      # dictionary: student name -> list of 'P' / 'A'
total_days = 0     # number of class days recorded so far


def add_students():
    names = input("Enter student name(s), separated by commas: ").split(",")
    added = []
    for n in names:
        n = n.strip().title()
        if n == "":
            continue
        if n in students:
            print(f"{n} already exists.")
        else:
            students[n] = ["A"] * total_days
            added.append(n)
    if added:
        print("Added:", ", ".join(added))


def mark_day():
    global total_days
    if not students:
        print("Add students first.")
        return
    absent = input("Enter absentees (comma separated, blank if none): ")
    absentees = [n.strip().title() for n in absent.split(",") if n.strip()]
    for n in absentees:
        if n not in students:
            print(f"Student '{n}' not found. Day not recorded.")
            return
    for name in students:
        students[name].append("A" if name in absentees else "P")
    total_days += 1
    print(f"Attendance recorded for Day {total_days}.")


def update_status():
    if total_days == 0:
        print("No attendance recorded yet.")
        return
    name = input("Enter student name: ").strip().title()
    if name not in students:
        print("Student not found.")
        return
    day = int(input(f"Enter day number (1-{total_days}): "))
    if day < 1 or day > total_days:
        print("Invalid day number.")
        return
    status = input("Enter status (P/A): ").strip().upper()
    if status not in ("P", "A"):
        print("Invalid status. Use P or A.")
        return
    students[name][day - 1] = status
    print(f"{name}'s attendance for Day {day} updated to {status}.")


def percentage(name):
    if total_days == 0:
        return 0.0
    return students[name].count("P") / total_days * 100


def display_records():
    if not students:
        print("No students added yet.")
        return
    header = f"{'Name':<8}" + "".join(f"{'D' + str(d):>4}" for d in range(1, total_days + 1))
    header += f"{'Present':>9}{'%':>8}"
    print(header)
    print("-" * len(header))
    for name, record in students.items():
        row = f"{name:<8}" + "".join(f"{s:>4}" for s in record)
        row += f"{record.count('P'):>9}{percentage(name):>7.1f}%"
        print(row)


def show_defaulters():
    threshold = float(input("Enter minimum attendance % required: "))
    low = {n: percentage(n) for n in students if percentage(n) < threshold}
    if not low:
        print("No students below the threshold.")
    else:
        print(f"Students below {threshold:.0f}%:")
        for n, p in low.items():
            print(f"  {n:<8}{p:>6.1f}%  - Attendance shortage")


# ---- Program starts here ----
while True:
    print("\n1.Add Student 2.Mark Day 3.Update 4.Display 5.Defaulters 6.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_students()
    elif choice == "2":
        mark_day()
    elif choice == "3":
        update_status()
    elif choice == "4":
        display_records()
    elif choice == "5":
        show_defaulters()
    elif choice == "6":
        print("Exiting Attendance Tracker.")
        break
    else:
        print("Invalid choice.")

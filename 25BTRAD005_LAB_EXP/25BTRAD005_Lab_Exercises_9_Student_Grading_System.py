# ============================================================
# Lab Exercise 9: Student Grading System
# Name   : Adhithi Vagmye
# USN    : 25BTRAD005
# ============================================================

def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

students = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks (0-100): "))
    while marks < 0 or marks > 100:
        marks = int(input("Invalid! Enter marks (0-100): "))
    students[name] = marks

print(f"\n{'Name':<10}{'Marks':>7}{'Grade':>7}{'Result':>8}")
print("-" * 32)
total = 0
for name, marks in students.items():
    grade = get_grade(marks)
    result = "Fail" if grade == "F" else "Pass"
    total += marks
    print(f"{name:<10}{marks:>7}{grade:>7}{result:>8}")
print("-" * 32)
print(f"Class Average: {total / len(students):.2f}")
topper = max(students, key=students.get)
print(f"Topper: {topper} ({students[topper]})")

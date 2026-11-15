# ============================================================
# Lab Exercise 13: CSV-Based Payroll Management System
# Name   : Adhithi Vagmye
# USN    : 25BTRAD005
# ============================================================
# Note: Needs a file named "employees.csv" in the same folder.
# Sample employees.csv content:
# emp_id,name,basic_salary
# E001,Rahul,40000
# E002,Priya,55000
# E003,Arjun,30000

import csv

print(f"{'ID':<6}{'Name':<8}{'Basic':>9}{'Gross':>10}{'PF':>8}{'Tax':>8}{'Net':>10}")
print("-" * 59)
rows, skipped = [], 0

with open("employees.csv", newline="") as f:
    for row in csv.DictReader(f):
        try:
            basic = float(row["basic_salary"])
            if basic <= 0:
                raise ValueError
        except ValueError:
            print(f"{row['emp_id']:<6}Invalid salary - record skipped")
            skipped += 1
            continue
        gross = basic + 0.20 * basic + 0.10 * basic      # Basic + HRA + DA
        pf = 0.12 * basic                                  # Provident Fund
        tax = 0.10 * gross if gross > 50000 else 0.05 * gross
        net = gross - pf - tax
        rows.append([row["emp_id"], row["name"], basic, gross, pf, tax, net])
        print(f"{row['emp_id']:<6}{row['name']:<8}{basic:>9.0f}{gross:>10.0f}{pf:>8.0f}{tax:>8.0f}{net:>10.0f}")

print("-" * 59)
print("Employees processed :", len(rows), "| Skipped:", skipped)
print(f"Total Gross Salary  : {sum(r[3] for r in rows):.2f}")
print(f"Total Deductions    : {sum(r[4] + r[5] for r in rows):.2f}")
print(f"Total Net Payout    : {sum(r[6] for r in rows):.2f}")
top = max(rows, key=lambda r: r[6])
print(f"Highest Net Salary  : {top[1]} ({top[6]:.2f})")

with open("salary_summary.csv", "w", newline="") as out:
    w = csv.writer(out)
    w.writerow(["emp_id", "name", "gross", "deductions", "net"])
    for r in rows:
        w.writerow([r[0], r[1], r[3], r[4] + r[5], r[6]])

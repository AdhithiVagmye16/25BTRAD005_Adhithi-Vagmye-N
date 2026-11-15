# ============================================================
# Lab Exercise 11: Log File Reader Program
# Name   : Adhithi Vagmye
# USN    : 25BTRAD005
# ============================================================

filename = input("Enter log file name: ")
counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}

try:
    with open(filename, "r") as f:
        lines = f.readlines()
    if len(lines) == 0:
        print("The log file is empty.")
    else:
        for line in lines:
            for key in counts:
                if key in line:
                    counts[key] += 1
        print("\nLog Summary:")
        for key, value in counts.items():
            print(f"{key:<8}: {value}")
        print("Total lines:", len(lines))
        if counts["ERROR"] > 0:
            print("Attention: errors found in the log!")
except FileNotFoundError:
    print("Error: File not found.")

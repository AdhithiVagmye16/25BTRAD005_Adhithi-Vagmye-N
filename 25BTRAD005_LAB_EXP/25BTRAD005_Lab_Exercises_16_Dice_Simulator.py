# ============================================================
# Lab Exercise 16: Dice Simulator using random Module
# Name   : Adhithi Vagmye
# USN    : 25BTRAD005
# ============================================================

import random

dice = int(input("Enter number of dice (1-3): "))
freq = {}
count = 0

while True:
    result = [random.randint(1, 6) for _ in range(dice)]
    total = sum(result)
    count += 1
    freq[total] = freq.get(total, 0) + 1
    print(f"Roll {count}: {result} -> Total = {total}")
    if input("Roll again? (y/n): ").lower() != "y":
        break

print("\nOutcome frequency for your rolls:")
for value in sorted(freq):
    print(f"{value:>3} : {'*' * freq[value]} ({freq[value]})")

# Repeated trials: 600 rolls of a single die
trial = {face: 0 for face in range(1, 7)}
for _ in range(600):
    trial[random.randint(1, 6)] += 1

print("\nFrequency in 600 rolls of one die:")
for face, c in trial.items():
    print(f"Face {face}: {c:>3} ({c / 600 * 100:.1f}%)")
print("Expected for each face: 100 (16.7%)")

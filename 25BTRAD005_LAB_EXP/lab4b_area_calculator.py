
# Lab Exercise 4B: Area Calculation

import math

print("---- Area Calculator ----")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")
print("4. Square")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    r = float(input("Enter radius: "))
    area = math.pi * r * r
    print(f"Area of Circle = {area:.2f}")

elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    area = l * w
    print(f"Area of Rectangle = {area:.2f}")

elif choice == 3:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print(f"Area of Triangle = {area:.2f}")

elif choice == 4:
    side = float(input("Enter side: "))
    area = side * side
    print(f"Area of Square = {area:.2f}")

else:
    print("Invalid choice")

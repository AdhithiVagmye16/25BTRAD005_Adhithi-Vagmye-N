
# Lab Exercise 3: Variables, Operators and Input/Output

# Get input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Arithmetic Operators
print("\n--- Arithmetic Operators ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Modulus:", a % b)
else:
    print("Division: Not possible (zero divisor)")
    print("Floor Division: Not possible")
    print("Modulus: Not possible")

print("Exponent:", a ** b)

# Comparison Operators
print("\n--- Comparison Operators ---")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)

# Logical Operators
print("\n--- Logical Operators ---")
print("(a > 0) and (b > 0):", (a > 0) and (b > 0))
print("(a > 0) or (b < 0):", (a > 0) or (b < 0))

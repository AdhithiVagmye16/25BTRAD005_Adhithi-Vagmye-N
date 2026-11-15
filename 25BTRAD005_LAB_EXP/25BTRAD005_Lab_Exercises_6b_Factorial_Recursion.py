# ============================================================
# Lab Exercise 6b: Factorial Program (using recursion)
# Name   : Adhithi Vagmye
# USN    : 25BTRAD005
# Dept   : B.Tech Computer Science Engineering (AI & Data Engineering)
# College: Jain University
# ============================================================
# Aim: Compute the factorial of a number using recursion.

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number to find its factorial: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")

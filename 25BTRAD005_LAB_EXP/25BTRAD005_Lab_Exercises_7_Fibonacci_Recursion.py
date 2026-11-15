# ============================================================
# Lab Exercise 7: Fibonacci Series using Recursion
# Name   : Adhithi Vagmye
# USN    : 25BTRAD005
# Dept   : B.Tech Computer Science Engineering (AI & Data Engineering)
# College: Jain University
# ============================================================
# Aim: Generate the Fibonacci series up to a given number of terms
#      using a recursive function.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter the number of terms: "))

print(f"\nFibonacci Series with {terms} terms:")
for i in range(terms):
    print(fibonacci(i), end=" ")
print()

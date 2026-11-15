# ============================================================
# Lab Exercise 6a: Prime Number Program
# Name   : Adhithi Vagmye
# USN    : 25BTRAD005
# Dept   : B.Tech Computer Science Engineering (AI & Data Engineering)
# College: Jain University
# ============================================================
# Aim: Check whether a given number is prime (iterative approach).

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number to check if it is prime: "))

if is_prime(num):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is Not a Prime Number.")

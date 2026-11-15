# ============================================================
# Lab Exercise 5: Number Guessing Game
# Name   : Adhithi Vagmye
# USN    : 25BTRAD005
# Dept   : B.Tech Computer Science Engineering (AI & Data Engineering)
# College: Jain University
# ============================================================
# Aim: Generate a random number and let the user guess it
#      within a limited number of attempts using random module and loops.

import random

def guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("=== Number Guessing Game ===")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.\n")
        elif guess > number:
            print("Too high! Try again.\n")
        else:
            print(f"\nCongratulations! You guessed it correctly in {attempts} attempts!")
            break
    else:
        print(f"\nGame Over! You've used all {max_attempts} attempts.")
        print(f"The correct number was {number}.")

# ---- Program starts here ----
guessing_game()

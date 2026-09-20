# ==========================================
# Mini Project - Number Guessing Game
# ==========================================

import random

print("==========================================")
print("       NUMBER GUESSING GAME")
print("==========================================")

secret_number = random.randint(1, 100)

max_attempts = 5
attempts = 0

while attempts < max_attempts:

    print()
    print("Attempt", attempts + 1, "/", max_attempts)

    guess = int(input("Guess the number (1-100): "))

    attempts += 1

    if guess > secret_number:
        print("Too high!")

    elif guess < secret_number:
        print("Too low!")

    else:
        print()
        print("Correct!")
        print("You guessed the number in", attempts, "attempts.")
        break

else:
    print()
    print("Game over!")
    print("You used all", max_attempts, "attempts.")
    print("The secret number was:", secret_number)

print("==========================================")
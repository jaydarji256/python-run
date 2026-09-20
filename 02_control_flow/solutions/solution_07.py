# ==========================================
# Solution 07 - Number Guessing Game
# ==========================================

secret_number = 7

while True:

    guess = int(input("Guess the number: "))

    if guess > secret_number:
        print("Too high")

    elif guess < secret_number:
        print("Too low")

    else:
        print("Correct!")
        break
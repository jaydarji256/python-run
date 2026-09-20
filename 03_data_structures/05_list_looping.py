# ==========================================
# 05 - Data Structures: Looping Through Lists
# ==========================================

fruits = ["apple", "banana", "orange", "mango"]

# ------------------------------------------
# 1. Basic for loop
# ------------------------------------------

for fruit in fruits:
    print(fruit)


# ------------------------------------------
# 2. Loop through numbers
# ------------------------------------------

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


# ------------------------------------------
# 3. Perform an operation on each element
# ------------------------------------------

for number in numbers:
    print(number * 2)


# ------------------------------------------
# 4. Check conditions while looping
# ------------------------------------------

for number in numbers:

    if number > 25:
        print(number, "is greater than 25")


# ------------------------------------------
# 5. Using enumerate()
# ------------------------------------------

for index, fruit in enumerate(fruits):
    print(index, fruit)
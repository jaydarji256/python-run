# ==========================================
# 01 - Functions: Basics
# ==========================================


# ------------------------------------------
# 1. A simple function
# ------------------------------------------

def greet():
    print("Hello, Python!")


# Calling the function
greet()


# ------------------------------------------
# 2. Calling a function multiple times
# ------------------------------------------

greet()
greet()


# ------------------------------------------
# 3. Function with a parameter
# ------------------------------------------

def greet_person(name):
    print("Hello,", name)


greet_person("Jay")
greet_person("Rahul")
greet_person("Amit")


# ------------------------------------------
# 4. Function with multiple parameters
# ------------------------------------------

def introduce(name, age):
    print("Name:", name)
    print("Age:", age)


introduce("Jay", 20)


# ------------------------------------------
# 5. Function with a calculation
# ------------------------------------------

def add_numbers(a, b):
    print("Sum:", a + b)


add_numbers(10, 20)
add_numbers(50, 30)


# ------------------------------------------
# 6. Function with a condition
# ------------------------------------------

def check_even(number):

    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")


check_even(10)
check_even(7)
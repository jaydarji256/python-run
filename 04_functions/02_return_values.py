# ==========================================
# 02 - Functions: Return Values
# ==========================================


# ------------------------------------------
# 1. Basic return
# ------------------------------------------

def add(a, b):
    return a + b


result = add(10, 20)

print("Result:", result)


# ------------------------------------------
# 2. Using the returned value
# ------------------------------------------

result = add(50, 30)

print("Result:", result)
print("Result multiplied by 2:", result * 2)


# ------------------------------------------
# 3. Return a string
# ------------------------------------------

def greet(name):
    return "Hello, " + name


message = greet("Jay")

print(message)


# ------------------------------------------
# 4. Return a boolean
# ------------------------------------------

def is_even(number):

    if number % 2 == 0:
        return True

    return False


print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))


# ------------------------------------------
# 5. Return from a condition
# ------------------------------------------

def check_age(age):

    if age >= 18:
        return "Adult"

    return "Minor"


print(check_age(20))
print(check_age(15))


# ------------------------------------------
# 6. Return multiple values
# ------------------------------------------

def calculate(a, b):

    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


results = calculate(10, 5)

print("Results:", results)


# ------------------------------------------
# 7. Unpacking returned values
# ------------------------------------------

addition, subtraction, multiplication = calculate(20, 10)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
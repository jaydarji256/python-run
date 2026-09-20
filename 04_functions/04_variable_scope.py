# ==========================================
# 04 - Functions: Variable Scope
# ==========================================


# ------------------------------------------
# 1. Local variable
# ------------------------------------------

def greet():
    message = "Hello from the function"

    print(message)


greet()


# ------------------------------------------
# 2. Local variables are only available
#    inside the function
# ------------------------------------------

def calculate():
    result = 10 + 20

    print("Inside function:", result)


calculate()

# This would cause an error because result
# only exists inside calculate():
#
# print(result)


# ------------------------------------------
# 3. Different functions can have variables
#    with the same name
# ------------------------------------------

def function_one():
    number = 10
    print("Function one:", number)


def function_two():
    number = 50
    print("Function two:", number)


function_one()
function_two()


# ------------------------------------------
# 4. Global variable
# ------------------------------------------

name = "Jay"


def show_name():
    print("Inside function:", name)


show_name()

print("Outside function:", name)


# ------------------------------------------
# 5. Local variable can have the same name
#    as a global variable
# ------------------------------------------

age = 20


def show_age():
    age = 25

    print("Inside function:", age)


show_age()

print("Outside function:", age)


# ------------------------------------------
# 6. Reading a global variable
# ------------------------------------------

tax_rate = 18


def calculate_tax(price):
    tax = price * tax_rate / 100

    return tax


print("Tax:", calculate_tax(1000))


# ------------------------------------------
# 7. Changing a global variable
# ------------------------------------------

counter = 0


def increase_counter():
    global counter

    counter += 1


increase_counter()
increase_counter()
increase_counter()

print("Counter:", counter)


# ------------------------------------------
# 8. Why local variables are usually better
# ------------------------------------------

def calculate_total(price, tax):
    total = price + (price * tax / 100)

    return total


total = calculate_total(1000, 18)

print("Total:", total)
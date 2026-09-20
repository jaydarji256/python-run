# ==========================================
# 03 - Functions: Arguments
# ==========================================


# ------------------------------------------
# 1. Positional arguments
# ------------------------------------------

def introduce(name, age):
    print("Name:", name)
    print("Age:", age)


introduce("Jay", 20)


# ------------------------------------------
# 2. Order matters with positional arguments
# ------------------------------------------

def student_info(name, branch, cgpa):
    print("Name:", name)
    print("Branch:", branch)
    print("CGPA:", cgpa)


student_info("Jay", "Computer Engineering", 7.3)


# ------------------------------------------
# 3. Keyword arguments
# ------------------------------------------

student_info(
    name="Jay",
    branch="Computer Engineering",
    cgpa=7.3
)


# ------------------------------------------
# 4. Keyword arguments can be in a
# different order
# ------------------------------------------

student_info(
    cgpa=7.3,
    name="Jay",
    branch="Computer Engineering"
)


# ------------------------------------------
# 5. Default arguments
# ------------------------------------------

def greet(name, message="Hello"):
    print(message, name)


greet("Jay")

greet("Rahul", "Welcome")


# ------------------------------------------
# 6. Multiple default arguments
# ------------------------------------------

def calculate_bill(price, tax=18, discount=0):

    final_price = price

    final_price += price * tax / 100
    final_price -= price * discount / 100

    return final_price


print("Bill 1:", calculate_bill(1000))

print(
    "Bill 2:",
    calculate_bill(
        1000,
        tax=18,
        discount=10
    )
)


# ------------------------------------------
# 7. Mixing positional and keyword arguments
# ------------------------------------------

def create_profile(name, age, city="Ahmedabad"):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)


create_profile("Jay", 20)

create_profile(
    "Jay",
    20,
    city="Ahmedabad"
)
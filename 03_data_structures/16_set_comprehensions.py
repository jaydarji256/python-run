# ==========================================
# 16 - Data Structures: Set Comprehensions
# ==========================================


# ------------------------------------------
# 1. Basic set comprehension
# ------------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = {number * number for number in numbers}

print("Squares:", squares)


# ------------------------------------------
# 2. Remove duplicates
# ------------------------------------------

numbers = [1, 2, 2, 3, 3, 4, 4, 5]

unique_numbers = {number for number in numbers}

print("Unique numbers:", unique_numbers)


# ------------------------------------------
# 3. Set comprehension with condition
# ------------------------------------------

even_numbers = {
    number
    for number in numbers
    if number % 2 == 0
}

print("Even numbers:", even_numbers)


# ------------------------------------------
# 4. Squares of even numbers
# ------------------------------------------

even_squares = {
    number * number
    for number in numbers
    if number % 2 == 0
}

print("Even squares:", even_squares)


# ------------------------------------------
# 5. Convert strings to uppercase
# ------------------------------------------

names = ["jay", "rahul", "jay", "amit", "rahul"]

uppercase_names = {
    name.upper()
    for name in names
}

print("Uppercase names:", uppercase_names)


# ------------------------------------------
# 6. Extract unique domains
# ------------------------------------------

emails = [
    "jay@gmail.com",
    "rahul@yahoo.com",
    "amit@gmail.com",
    "neha@outlook.com",
    "alex@yahoo.com"
]

domains = {
    email.split("@")[1]
    for email in emails
}

print("Email domains:", domains)
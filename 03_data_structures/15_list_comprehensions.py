# ==========================================
# 15 - Data Structures: List Comprehensions
# ==========================================

# ------------------------------------------
# 1. Basic list comprehension
# ------------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print("Squares:", squares)


# ------------------------------------------
# 2. Normal for loop vs comprehension
# ------------------------------------------

squares_loop = []

for number in numbers:
    squares_loop.append(number * number)

print("Using loop:", squares_loop)

squares_comprehension = [number * number for number in numbers]

print("Using comprehension:", squares_comprehension)


# ------------------------------------------
# 3. With a condition
# ------------------------------------------

even_numbers = [number for number in numbers if number % 2 == 0]

print("Even numbers:", even_numbers)


# ------------------------------------------
# 4. Squares of even numbers
# ------------------------------------------

even_squares = [
    number * number
    for number in numbers
    if number % 2 == 0
]

print("Even squares:", even_squares)


# ------------------------------------------
# 5. Convert strings
# ------------------------------------------

names = ["jay", "rahul", "amit", "neha"]

uppercase_names = [name.upper() for name in names]

print("Uppercase names:", uppercase_names)


# ------------------------------------------
# 6. Extract values from a dictionary
# ------------------------------------------

students = {
    "Jay": 7.3,
    "Rahul": 8.1,
    "Amit": 7.8,
    "Neha": 8.5
}

high_cgpa = [
    name
    for name, cgpa in students.items()
    if cgpa >= 8
]

print("Students with CGPA >= 8:", high_cgpa)


# ------------------------------------------
# 7. Convert temperatures
# ------------------------------------------

celsius = [0, 10, 20, 30, 40]

fahrenheit = [
    (temperature * 9 / 5) + 32
    for temperature in celsius
]

print("Fahrenheit:", fahrenheit)
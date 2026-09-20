# ==========================================
# 17 - Data Structures: Dictionary Comprehensions
# ==========================================


# ------------------------------------------
# 1. Basic dictionary comprehension
# ------------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = {
    number: number * number
    for number in numbers
}

print("Squares:", squares)


# ------------------------------------------
# 2. Dictionary with a condition
# ------------------------------------------

even_squares = {
    number: number * number
    for number in numbers
    if number % 2 == 0
}

print("Even squares:", even_squares)


# ------------------------------------------
# 3. Convert list of names into dictionary
# ------------------------------------------

names = ["Jay", "Rahul", "Amit", "Neha"]

name_lengths = {
    name: len(name)
    for name in names
}

print("Name lengths:", name_lengths)


# ------------------------------------------
# 4. Create dictionary from two lists
# ------------------------------------------

students = ["Jay", "Rahul", "Amit"]
cgpas = [7.3, 8.1, 7.8]

student_cgpa = {
    name: cgpa
    for name, cgpa in zip(students, cgpas)
}

print("Student CGPAs:", student_cgpa)


# ------------------------------------------
# 5. Filter a dictionary
# ------------------------------------------

student_cgpa = {
    "Jay": 7.3,
    "Rahul": 8.1,
    "Amit": 7.8,
    "Neha": 8.5,
    "Alex": 6.9
}

high_cgpa_students = {
    name: cgpa
    for name, cgpa in student_cgpa.items()
    if cgpa >= 8
}

print("CGPA >= 8:", high_cgpa_students)


# ------------------------------------------
# 6. Convert temperatures
# ------------------------------------------

celsius = {
    "Monday": 25,
    "Tuesday": 28,
    "Wednesday": 30
}

fahrenheit = {
    day: (temperature * 9 / 5) + 32
    for day, temperature in celsius.items()
}

print("Fahrenheit:", fahrenheit)
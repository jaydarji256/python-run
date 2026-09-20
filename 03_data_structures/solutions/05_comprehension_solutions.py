# ==========================================
# 05 - Comprehension Exercise Solutions
# ==========================================


# Exercise 1
numbers = range(1, 21)

squares = [
    number ** 2
    for number in numbers
]

print("Squares:", squares)


# Exercise 2
numbers = range(1, 51)

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print("Even numbers:", even_numbers)


# Exercise 3
numbers = range(1, 21)

odd_cubes = [
    number ** 3
    for number in numbers
    if number % 2 != 0
]

print("Odd cubes:", odd_cubes)


# Exercise 4
names = [
    "Jay",
    "Rahul",
    "Amit",
    "Neha",
    "Alex",
    "Ankit"
]

first_letters = {
    name[0]
    for name in names
}

print("Unique first letters:", first_letters)


# Exercise 5
numbers = range(1, 11)

number_squares = {
    number: number ** 2
    for number in numbers
}

print("Number -> Square:", number_squares)


# Exercise 6
students = {
    "Jay": 7.3,
    "Rahul": 8.4,
    "Amit": 7.9,
    "Neha": 8.7
}

high_cgpa_students = {
    name: cgpa
    for name, cgpa in students.items()
    if cgpa >= 8
}

print("CGPA >= 8:", high_cgpa_students)
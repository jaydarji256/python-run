# ==========================================
# 03 - Set Exercise Solutions
# ==========================================

# Exercise 1
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union:", set_a | set_b)


# Exercise 2
print("Intersection:", set_a & set_b)


# Exercise 3
print("Only in A:", set_a - set_b)


# Exercise 4
print("Symmetric difference:", set_a ^ set_b)


# Exercise 5
numbers = [1, 2, 2, 3, 4, 4, 5, 5]

unique_numbers = set(numbers)

print("Unique numbers:", unique_numbers)


# Exercise 6
python_students = {
    "Jay",
    "Rahul",
    "Amit",
    "Neha"
}

ml_students = {
    "Rahul",
    "Amit",
    "Priya",
    "Alex"
}

both_courses = python_students & ml_students

print("Students in both courses:", both_courses)
# ==========================================
# 13 - Data Structures: Looping Through Dictionaries
# ==========================================

student = {
    "name": "Jay",
    "age": 20,
    "cgpa": 7.3,
    "branch": "Computer Engineering"
}


# ------------------------------------------
# 1. Loop through keys
# ------------------------------------------

print("Keys:")

for key in student:
    print(key)


# ------------------------------------------
# 2. Loop through values
# ------------------------------------------

print("\nValues:")

for value in student.values():
    print(value)


# ------------------------------------------
# 3. Loop through keys using keys()
# ------------------------------------------

print("\nKeys using keys():")

for key in student.keys():
    print(key)


# ------------------------------------------
# 4. Loop through key-value pairs
# ------------------------------------------

print("\nKey-value pairs:")

for key, value in student.items():
    print(key, ":", value)


# ------------------------------------------
# 5. Using a condition
# ------------------------------------------

print("\nChecking student information:")

for key, value in student.items():

    if key == "cgpa":
        print("Student CGPA:", value)


# ------------------------------------------
# 6. Dictionary with multiple students
# ------------------------------------------

students = {
    "Jay": 7.3,
    "Rahul": 8.1,
    "Amit": 7.8,
    "Neha": 8.5
}

print("\nStudent CGPAs:")

for name, cgpa in students.items():
    print(name, ":", cgpa)


# ------------------------------------------
# 7. Find students with CGPA >= 8
# ------------------------------------------

print("\nStudents with CGPA >= 8:")

for name, cgpa in students.items():

    if cgpa >= 8:
        print(name, ":", cgpa)
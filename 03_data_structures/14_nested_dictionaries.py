# ==========================================
# 14 - Data Structures: Nested Dictionaries
# ==========================================

# ------------------------------------------
# 1. Dictionary containing dictionaries
# ------------------------------------------

students = {
    "student_1": {
        "name": "Jay",
        "age": 20,
        "cgpa": 7.3
    },

    "student_2": {
        "name": "Rahul",
        "age": 21,
        "cgpa": 8.1
    },

    "student_3": {
        "name": "Amit",
        "age": 20,
        "cgpa": 7.8
    }
}

print(students)


# ------------------------------------------
# 2. Accessing nested data
# ------------------------------------------

print("Student 1:", students["student_1"])

print("Name:", students["student_1"]["name"])

print("CGPA:", students["student_1"]["cgpa"])


# ------------------------------------------
# 3. Updating nested data
# ------------------------------------------

students["student_1"]["cgpa"] = 7.5

print("Updated CGPA:", students["student_1"]["cgpa"])


# ------------------------------------------
# 4. Adding data to a nested dictionary
# ------------------------------------------

students["student_1"]["city"] = "Ahmedabad"

print(students["student_1"])


# ------------------------------------------
# 5. Looping through nested dictionaries
# ------------------------------------------

for student_id, student_data in students.items():

    print()
    print("Student ID:", student_id)

    for key, value in student_data.items():
        print(key, ":", value)


# ------------------------------------------
# 6. Finding students with CGPA >= 8
# ------------------------------------------

print()
print("Students with CGPA >= 8:")

for student_id, student_data in students.items():

    if student_data["cgpa"] >= 8:
        print(student_data["name"], student_data["cgpa"])
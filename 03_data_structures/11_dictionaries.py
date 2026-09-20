# ==========================================
# 11 - Data Structures: Dictionaries
# ==========================================

# ------------------------------------------
# 1. Creating a dictionary
# ------------------------------------------

student = {
    "name": "Jay",
    "age": 20,
    "cgpa": 7.3,
    "branch": "Computer Engineering"
}

print(student)


# ------------------------------------------
# 2. Accessing values
# ------------------------------------------

print("Name:", student["name"])
print("Age:", student["age"])
print("CGPA:", student["cgpa"])


# ------------------------------------------
# 3. Using get()
# ------------------------------------------

print("Branch:", student.get("branch"))

# get() safely handles missing keys
print("City:", student.get("city"))


# ------------------------------------------
# 4. Adding a new key-value pair
# ------------------------------------------

student["city"] = "Ahmedabad"

print(student)


# ------------------------------------------
# 5. Updating a value
# ------------------------------------------

student["cgpa"] = 7.5

print("Updated CGPA:", student["cgpa"])


# ------------------------------------------
# 6. Checking if a key exists
# ------------------------------------------

if "name" in student:
    print("Name exists in dictionary")


# ------------------------------------------
# 7. Checking if a key does not exist
# ------------------------------------------

if "email" not in student:
    print("Email does not exist")


# ------------------------------------------
# 8. Number of key-value pairs
# ------------------------------------------

print("Number of entries:", len(student))
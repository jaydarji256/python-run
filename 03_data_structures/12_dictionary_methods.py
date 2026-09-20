# ==========================================
# 12 - Data Structures: Dictionary Methods
# ==========================================

student = {
    "name": "Jay",
    "age": 20,
    "cgpa": 7.3,
    "branch": "Computer Engineering"
}


# ------------------------------------------
# 1. keys()
# ------------------------------------------

print("Keys:")
print(student.keys())


# ------------------------------------------
# 2. values()
# ------------------------------------------

print("Values:")
print(student.values())


# ------------------------------------------
# 3. items()
# ------------------------------------------

print("Items:")
print(student.items())


# ------------------------------------------
# 4. update()
# ------------------------------------------

student.update({
    "age": 21,
    "cgpa": 7.5
})

print("After update:")
print(student)


# ------------------------------------------
# 5. pop()
# ------------------------------------------

removed_value = student.pop("branch")

print("Removed:", removed_value)
print("After pop:")
print(student)


# ------------------------------------------
# 6. popitem()
# ------------------------------------------

removed_item = student.popitem()

print("Removed item:", removed_item)
print("After popitem:")
print(student)


# ------------------------------------------
# 7. setdefault()
# ------------------------------------------

student.setdefault("city", "Ahmedabad")

print("After setdefault:")
print(student)


# ------------------------------------------
# 8. copy()
# ------------------------------------------

student_copy = student.copy()

print("Copied dictionary:")
print(student_copy)


# ------------------------------------------
# 9. clear()
# ------------------------------------------

temporary = {
    "name": "Alex",
    "age": 21
}

temporary.clear()

print("After clear:")
print(temporary)
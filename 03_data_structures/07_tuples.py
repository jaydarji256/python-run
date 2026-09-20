# ==========================================
# 07 - Data Structures: Tuples
# ==========================================

# ------------------------------------------
# 1. Creating a tuple
# ------------------------------------------

fruits = ("apple", "banana", "orange", "mango")

print(fruits)


# ------------------------------------------
# 2. Accessing tuple elements
# ------------------------------------------

print("First:", fruits[0])
print("Last:", fruits[-1])


# ------------------------------------------
# 3. Tuple with different data types
# ------------------------------------------

student = ("Jay", 20, 7.3, True)

print(student)


# ------------------------------------------
# 4. Tuple length
# ------------------------------------------

print("Length:", len(fruits))


# ------------------------------------------
# 5. Looping through a tuple
# ------------------------------------------

for fruit in fruits:
    print(fruit)


# ------------------------------------------
# 6. Tuple unpacking
# ------------------------------------------

name, age, cgpa, passed = student

print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print("Passed:", passed)
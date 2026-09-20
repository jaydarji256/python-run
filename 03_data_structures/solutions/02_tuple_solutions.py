# ==========================================
# 02 - Tuple Exercise Solutions
# ==========================================

# Exercise 1
numbers = (10, 25, 7, 42, 18)

largest = max(numbers)

print("Largest:", largest)


# Exercise 2
numbers = (10, 20, 10, 30, 10, 40)

print("Count of 10:", numbers.count(10))


# Exercise 3
student = ("Jay", 20, "Computer Engineering", 7.3)

name, age, branch, cgpa = student

print("Name:", name)
print("Age:", age)
print("Branch:", branch)
print("CGPA:", cgpa)


# Exercise 4
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)

combined = tuple_a + tuple_b

print("Combined:", combined)


# Exercise 5
numbers = (10, 20, 30, 40, 50, 60)

middle = numbers[2:5]

print("Middle elements:", middle)
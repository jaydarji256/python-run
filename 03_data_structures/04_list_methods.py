# ==========================================
# 04 - Data Structures: List Methods
# ==========================================

fruits = ["apple", "banana", "orange"]

# ------------------------------------------
# 1. append()
# ------------------------------------------

fruits.append("mango")
print("After append:", fruits)


# ------------------------------------------
# 2. insert()
# ------------------------------------------

fruits.insert(1, "grapes")
print("After insert:", fruits)


# ------------------------------------------
# 3. remove()
# ------------------------------------------

fruits.remove("banana")
print("After remove:", fruits)


# ------------------------------------------
# 4. pop()
# ------------------------------------------

removed_fruit = fruits.pop()
print("Removed:", removed_fruit)
print("After pop:", fruits)


# ------------------------------------------
# 5. pop(index)
# ------------------------------------------

removed_fruit = fruits.pop(1)
print("Removed:", removed_fruit)
print("After pop(index):", fruits)


# ------------------------------------------
# 6. sort()
# ------------------------------------------

numbers = [50, 10, 40, 20, 30]

numbers.sort()
print("Sorted:", numbers)


# ------------------------------------------
# 7. reverse()
# ------------------------------------------

numbers.reverse()
print("Reversed:", numbers)


# ------------------------------------------
# 8. count()
# ------------------------------------------

numbers = [10, 20, 10, 30, 10, 40]

print("10 appears:", numbers.count(10), "times")


# ------------------------------------------
# 9. index()
# ------------------------------------------

print("Index of 30:", numbers.index(30))


# ------------------------------------------
# 10. len()
# ------------------------------------------

print("Number of elements:", len(numbers))
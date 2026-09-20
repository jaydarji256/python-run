# ==========================================
# 09 - Data Structures: Sets
# ==========================================

# ------------------------------------------
# 1. Creating a set
# ------------------------------------------

fruits = {"apple", "banana", "orange", "apple"}

print("Fruits:", fruits)


# ------------------------------------------
# 2. Duplicate values are removed
# ------------------------------------------

numbers = {1, 2, 3, 2, 4, 3, 5}

print("Numbers:", numbers)


# ------------------------------------------
# 3. Adding an element
# ------------------------------------------

numbers.add(6)

print("After add:", numbers)


# ------------------------------------------
# 4. Removing an element
# ------------------------------------------

numbers.remove(3)

print("After remove:", numbers)


# ------------------------------------------
# 5. Discarding an element
# ------------------------------------------

numbers.discard(100)

print("After discard:", numbers)


# ------------------------------------------
# 6. Membership checking
# ------------------------------------------

print("Is 5 present?", 5 in numbers)
print("Is 100 present?", 100 in numbers)


# ------------------------------------------
# 7. Length
# ------------------------------------------

print("Number of elements:", len(numbers))


# ------------------------------------------
# 8. Looping through a set
# ------------------------------------------

for number in numbers:
    print(number)
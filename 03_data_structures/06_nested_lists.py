# ==========================================
# 06 - Data Structures: Nested Lists
# ==========================================

# ------------------------------------------
# 1. Creating a nested list
# ------------------------------------------

students = [
    ["Jay", 20, 7.3],
    ["Rahul", 21, 8.1],
    ["Amit", 20, 7.8]
]

print(students)


# ------------------------------------------
# 2. Accessing nested list elements
# ------------------------------------------

print(students[0])
print(students[0][0])
print(students[0][1])
print(students[0][2])


# ------------------------------------------
# 3. Another example - matrix
# ------------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)


# ------------------------------------------
# 4. Accessing matrix elements
# ------------------------------------------

print(matrix[0][0])
print(matrix[1][1])
print(matrix[2][2])


# ------------------------------------------
# 5. Looping through a nested list
# ------------------------------------------

for row in matrix:
    print(row)


# ------------------------------------------
# 6. Nested loop
# ------------------------------------------

for row in matrix:

    for value in row:
        print(value, end=" ")

    print()
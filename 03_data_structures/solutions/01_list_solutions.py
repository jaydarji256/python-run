# ==========================================
# 01 - List Exercise Solutions
# ==========================================

# Exercise 1
numbers = [10, 25, 7, 42, 18, 91, 33, 5, 64, 20]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest:", largest)


# Exercise 2
numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

print("Sum:", total)


# Exercise 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print("Even numbers:", even_numbers)


# Exercise 4
numbers = [1, 2, 3, 2, 4, 1, 5, 3]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("Unique numbers:", unique_numbers)


# Exercise 5
numbers = [1, 2, 3, 4, 5]

reversed_numbers = []

for number in numbers:
    reversed_numbers.insert(0, number)

print("Reversed:", reversed_numbers)


# Exercise 6
numbers = [10, 20, 10, 30, 10, 40]

target = 10
count = 0

for number in numbers:
    if number == target:
        count += 1

print("Count:", count)


# Exercise 7
numbers = [10, 50, 20, 80, 30, 70]

unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)

second_largest = unique_numbers[1]

print("Second largest:", second_largest)


# Exercise 8
names = ["Jay", "Rahul", "Amit", "Alexander", "Neha"]

for name in names:
    if len(name) > 5:
        print("Long name:", name)
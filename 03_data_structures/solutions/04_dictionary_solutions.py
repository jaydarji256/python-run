# ==========================================
# 04 - Dictionary Exercise Solutions
# ==========================================

# Exercise 1
students = {
    "Jay": 7.3,
    "Rahul": 8.1,
    "Amit": 7.8,
    "Neha": 8.5,
    "Alex": 6.9
}

for name, cgpa in students.items():
    print(name, ":", cgpa)


# Exercise 2
highest_student = None
highest_cgpa = 0

for name, cgpa in students.items():

    if cgpa > highest_cgpa:
        highest_cgpa = cgpa
        highest_student = name

print("Highest CGPA:", highest_student)
print("CGPA:", highest_cgpa)


# Exercise 3
total = 0

for cgpa in students.values():
    total += cgpa

average = total / len(students)

print("Average CGPA:", average)


# Exercise 4
print("Students with CGPA >= 8:")

for name, cgpa in students.items():

    if cgpa >= 8:
        print(name, ":", cgpa)


# Exercise 5
products = {
    "Laptop": 80000,
    "Phone": 50000,
    "Mouse": 1500,
    "Monitor": 20000
}

most_expensive = None
highest_price = 0

for product, price in products.items():

    if price > highest_price:
        highest_price = price
        most_expensive = product

print("Most expensive:", most_expensive)
print("Price:", highest_price)


# Exercise 6
employees = {
    "Alice": 50000,
    "Bob": 65000,
    "Charlie": 45000,
    "David": 80000
}

total_salary = 0

for salary in employees.values():
    total_salary += salary

print("Total salary:", total_salary)


# Exercise 7
employees = {
    "emp1": {
        "name": "Alice",
        "role": "Developer"
    },

    "emp2": {
        "name": "Bob",
        "role": "Data Scientist"
    },

    "emp3": {
        "name": "Charlie",
        "role": "ML Engineer"
    }
}

for employee_id, employee in employees.items():

    print(
        employee["name"],
        ":",
        employee["role"]
    )
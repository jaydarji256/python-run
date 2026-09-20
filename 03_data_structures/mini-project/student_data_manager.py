# ==========================================
# 03 Data Structures - Mini Project
# Student Data Manager
# ==========================================


students = [
    {
        "name": "Jay",
        "age": 20,
        "branch": "Computer Engineering",
        "cgpa": 7.3,
        "skills": ["Python", "SQL", "Machine Learning"]
    },

    {
        "name": "Rahul",
        "age": 21,
        "branch": "Computer Engineering",
        "cgpa": 8.1,
        "skills": ["Java", "Python", "Docker"]
    },

    {
        "name": "Amit",
        "age": 20,
        "branch": "Information Technology",
        "cgpa": 7.8,
        "skills": ["Python", "JavaScript", "SQL"]
    },

    {
        "name": "Neha",
        "age": 21,
        "branch": "Computer Engineering",
        "cgpa": 8.5,
        "skills": ["Python", "Machine Learning", "TensorFlow"]
    }
]


# ==========================================
# 1. Display all students
# ==========================================

print("========== ALL STUDENTS ==========")

for student in students:
    print(student["name"], "-", student["cgpa"])


# ==========================================
# 2. Find students with CGPA >= 8
# ==========================================

print("\n========== CGPA >= 8 ==========")

for student in students:

    if student["cgpa"] >= 8:
        print(student["name"], "-", student["cgpa"])


# ==========================================
# 3. Calculate average CGPA
# ==========================================

total_cgpa = 0

for student in students:
    total_cgpa += student["cgpa"]

average_cgpa = total_cgpa / len(students)

print("\nAverage CGPA:", average_cgpa)


# ==========================================
# 4. Find highest CGPA
# ==========================================

highest_student = students[0]

for student in students:

    if student["cgpa"] > highest_student["cgpa"]:
        highest_student = student

print("\nHighest CGPA:")
print(highest_student["name"], "-", highest_student["cgpa"])


# ==========================================
# 5. Get all unique skills
# ==========================================

all_skills = set()

for student in students:

    for skill in student["skills"]:
        all_skills.add(skill)

print("\n========== UNIQUE SKILLS ==========")

for skill in all_skills:
    print(skill)


# ==========================================
# 6. Find students who know Python
# ==========================================

print("\n========== PYTHON STUDENTS ==========")

for student in students:

    if "Python" in student["skills"]:
        print(student["name"])


# ==========================================
# 7. Create a list of student names
# ==========================================

student_names = [
    student["name"]
    for student in students
]

print("\nStudent names:", student_names)


# ==========================================
# 8. Create dictionary: name -> CGPA
# ==========================================

student_cgpa = {
    student["name"]: student["cgpa"]
    for student in students
}

print("\nName -> CGPA:")
print(student_cgpa)


# ==========================================
# 9. Students with CGPA >= 8
# ==========================================

high_cgpa_students = {
    student["name"]: student["cgpa"]
    for student in students
    if student["cgpa"] >= 8
}

print("\nHigh CGPA students:")
print(high_cgpa_students)


# ==========================================
# 10. Branches
# ==========================================

branches = {
    student["branch"]
    for student in students
}

print("\nBranches:")
print(branches)
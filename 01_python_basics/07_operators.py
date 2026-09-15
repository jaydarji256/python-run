# ==========================================
# 07 - Operators
# ==========================================

a = 10
b = 3


# ------------------------------------------
# Arithmetic Operators
# ------------------------------------------

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


# ------------------------------------------
# Comparison Operators
# ------------------------------------------

print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)


# ------------------------------------------
# Assignment Operators
# ------------------------------------------

x = 10

x += 5
print("x += 5:", x)

x -= 3
print("x -= 3:", x)

x *= 2
print("x *= 2:", x)

x /= 4
print("x /= 4:", x)


# ------------------------------------------
# Logical Operators
# ------------------------------------------

age = 20
has_id = True

print("AND:", age >= 18 and has_id)
print("OR:", age >= 18 or has_id)
print("NOT:", not has_id)
# ==========================================
# Solution 05 - Sum of Numbers
# ==========================================

n = int(input("Enter n: "))

total = 0

for number in range(1, n + 1):
    total += number

print("Sum:", total)
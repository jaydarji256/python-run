# ==========================================
# Solution 06 - Count Even and Odd Numbers
# ==========================================

even_count = 0
odd_count = 0

for number in range(1, 21):

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
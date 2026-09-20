# ==========================================
# 10 - Data Structures: Set Operations
# ==========================================

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}


# ------------------------------------------
# 1. Union
# ------------------------------------------

union = set_a | set_b

print("Union:", union)


# ------------------------------------------
# 2. Intersection
# ------------------------------------------

intersection = set_a & set_b

print("Intersection:", intersection)


# ------------------------------------------
# 3. Difference
# ------------------------------------------

difference_a = set_a - set_b
difference_b = set_b - set_a

print("A - B:", difference_a)
print("B - A:", difference_b)


# ------------------------------------------
# 4. Symmetric Difference
# ------------------------------------------

symmetric_difference = set_a ^ set_b

print("Symmetric Difference:", symmetric_difference)


# ------------------------------------------
# 5. Using methods instead of operators
# ------------------------------------------

print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("A - B:", set_a.difference(set_b))


# ------------------------------------------
# 6. Subset
# ------------------------------------------

small_set = {1, 2, 3}

print("Is small_set a subset of set_a?",
      small_set.issubset(set_a))


# ------------------------------------------
# 7. Superset
# ------------------------------------------

print("Is set_a a superset of small_set?",
      set_a.issuperset(small_set))


# ------------------------------------------
# 8. Disjoint
# ------------------------------------------

set_c = {10, 20, 30}

print("Are set_a and set_c disjoint?",
      set_a.isdisjoint(set_c))
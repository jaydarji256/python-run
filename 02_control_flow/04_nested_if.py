# ==========================================
# 04 - Control Flow: Nested if
# ==========================================

age = 20
has_id = True

if age >= 18:
    print("You are an adult.")

    if has_id:
        print("You have a valid ID.")
    else:
        print("You do not have an ID.")

else:
    print("You are a minor.")
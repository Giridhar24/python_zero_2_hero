# Topic of the Day: Conditionals (if, elif, else)
# Explanation: Code usually runs from top to bottom. Conditionals allow the code to branch.
# If a condition is True, it runs one block of code; if False, it skips it.
# Python relies on indentation (spacing) to know which code belongs inside the "if" block.

user_input = 75

# 1. The 'if' statement checks a condition
if user_input >= 90:
    print("Grade: A")

# 2. 'elif' (else if) runs ONLY if the previous checks failed
elif user_input >= 70:
    print("Grade: B")  # This will print because 75 >= 70

# 3. 'else' catches everything else (no condition needed)
else:
    print("Grade: C or lower")

# 4. Logical Operators (and, or)
# Checks if BOTH conditions are true
if user_input > 0 and user_input < 100:
    print("Valid score detected.")

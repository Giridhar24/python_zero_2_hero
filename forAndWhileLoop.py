# Topic of the Day: Loops (for and while)
# Explanation: Loops allow you to run the same block of code multiple times.
# for loop: Used when you know exactly how many times to loop (or iterating over a list).
# while loop: Used when you want to loop until a specific condition changes.

# 1. The 'for' loop with range()
# range(5) generates numbers 0, 1, 2, 3, 4
print("--- For Loop ---")
for i in range(5):
    print(f"Iteration: {i}")

# 2. Iterating over a list
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# 3. The 'while' loop
print("\n--- While Loop ---")
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count = count - 1  # Crucial: Update variables to avoid infinite loops!
print("Liftoff!")
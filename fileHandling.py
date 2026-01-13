# Topic of the Day: File Handling (open, read, write)
# Explanation: To read or write a file, you must "open" it.
# Best Practice: Use the with keyword.
# It creates a "Context Manager" that automatically closes the file even if your code crashes. This prevents memory leaks.

# 1. Writing to a file ('w' mode overwrites existing content)
with open("notes.txt", "w") as file:
    file.write("Day 9 Log:\n")
    file.write("Learning File I/O is crucial.")

# 2. Appending to a file ('a' mode adds to the end)
with open("notes.txt", "a") as file:
    file.write("\nThis line is added later.")

# 3. Reading a file ('r' mode)
with open("notes.txt", "r") as file:
    content = file.read()
    print("--- File Content ---")
    print(content)
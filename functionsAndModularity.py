# Topic of the Day: Functions (def and return)
# Explanation: A function in Python is defined using def.
# Parameters: Variables listed inside the parentheses () that the function receives as input.
# Return: The return keyword sends a value back to where the function was called. Without it, the function returns None.

# 1. Defining a function
def calculate_area(length, width):
    """
    Calculates area of a rectangle.
    """
    area = length * width
    return area  # Sends the result back

# 2. Calling the function
# We capture the returned value in a variable named 'result'
result = calculate_area(10, 5)

print(f"The area is: {result}")

# 3. Default Arguments
# If 'name' isn't provided, it defaults to "User"
def greet(name="User"):
    print(f"Hello, {name}!")

greet()          # Prints: Hello, User!
greet("Alice")   # Prints: Hello, Alice!
# Topic of the Day: Variables and Dynamic Typing

# Explanation: In Python, you don't need to declare the "type" of variable (like integer or string) explicitly.
# Python figures it out based on the value you assign. This is called dynamic typing.
# Variables are essentially labels or "nametags" attached to values.

# 1. Assignment
x = 10           # x is an integer
y = 3.14         # y is a float
name = "Hero"    # name is a string

# 2. Dynamic Typing in action
# We can change 'x' from an int to a string without error
print(f"Original x: {x} (Type: {type(x)})")

x = "Ten"
print(f"New x: {x} (Type: {type(x)})")

# 3. Basic Operation
# Python handles mixed types (int * float = float)
result = y * 2
print(f"Math Result: {result}")
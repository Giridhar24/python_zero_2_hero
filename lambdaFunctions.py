# Topic of the Day: Lambda Functions
# Explanation: A Lambda is a small, anonymous function defined in a single line.
# It is used when you need a short function for a short period of time (e.g., inside another function) and don't want to formally define it with def.
# Syntax: lambda arguments: expression

# 1. Standard Function
def add(a, b):
    return a + b

# 2. Equivalent Lambda
# "Take a and b, return a + b"
add_lambda = lambda a, b: a + b

print(add_lambda(5, 3)) # Output: 8

# 3. Real-world use: Sorting complex lists
# Sort a list of tuples based on the SECOND number (index 1)
pairs = [(1, 50), (2, 10), (3, 30)]

# The key is a lambda that grabs the second item from each pair
pairs.sort(key=lambda x: x[1])

print(f"Sorted by 2nd item: {pairs}")
# Output: [(2, 10), (3, 30), (1, 50)]
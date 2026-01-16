# Topic of the Day: Generators (yield)
# Explanation: Standard lists load everything into memory at once.
# If you list 1 billion numbers, your computer crashes.
# Generators produce one item at a time, on demand.
# They are memory efficient.
# You use the keyword yield instead of return.

# 1. Standard Function (Memory Heavy)
def get_squares_list(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result

# 2. Generator Function (Memory Efficient)
def get_squares_gen(n):
    for i in range(n):
        yield i * i  # Pauses here and gives one value

# Usage
# This creates a generator object, it doesn't calculate anything yet!
my_gen = get_squares_gen(5)

# We ask for the next value manually or via loop
print(next(my_gen)) # Output: 0
print(next(my_gen)) # Output: 1
print(next(my_gen)) # Output: 4

print("--- Loop through the rest ---")
for num in my_gen:
    print(num)
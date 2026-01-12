# Topic of the Day: Modules & Imports
# Explanation: A Module is simply a Python file (.py) containing functions and variables.
# You "Import" it into another file to use its code. This keeps your main program clean.
# import module_name: Imports everything.
# from module_name import specific_function: Imports only what you need (saves memory).

# Option 1: Import the whole file
import my_math

print(my_math.add(10, 5))

# Option 2: Import specific tools (Cleaner)
from my_math import subtract

print(subtract(10, 5))

# Option 3: Alias (Renaming for laziness)
import my_math as mm
print(mm.add(2, 2))
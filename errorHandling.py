# Topic of the Day: Error Handling (try, except)
# Explanation: Errors are inevitable. Instead of letting the program crash and show a scary red error message, we "catch" the error and handle it gracefully.
# try: Run this code.
# except: If an error happens, run this code instead.
# finally: Run this code no matter what (good for cleanup).

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")

    except TypeError:
        print("Error: Please provide numbers, not text.")

    finally:
        print("Operation attempted.")


# Test Cases
divide_numbers(10, 2)  # Works
divide_numbers(10, 0)  # Catches ZeroDivisionError
divide_numbers(10, "A")  # Catches TypeError
# Explanation: A Decorator is a design pattern that allows you to modify the behavior of a function without changing its code.
# It "wraps" the original function.
# Syntax: You see this often in web frameworks (like Flask/Django) as @app.route or @login_required.


# 1. The Decorator Function (The Wrapper)
def my_decorator(func):
    def wrapper():
        print("Something is happening BEFORE the function is called.")
        func()
        print("Something is happening AFTER the function is called.")
    return wrapper

# 2. Applying the Decorator
@my_decorator
def say_hello():
    print("Hello!")

# 3. Execution
# When we call say_hello, it actually runs the 'wrapper' inside 'my_decorator'
say_hello()

# Output:
# Something is happening BEFORE...
# Hello!
# Something is happening AFTER...
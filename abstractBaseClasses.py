# Topic of the Day: Abstract Base Classes (ABCs)
# Explanation: Python is loose with rules, but sometimes you want strictness.
# If you are building a system where every "Shape" must have an area calculation, you use an Abstract Base Class.
# It forces any child class to write that method, or else Python will throw an error.

from abc import ABC, abstractmethod


# 1. The Abstract Contract
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# 2. Concrete Class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # We MUST implement 'area', otherwise 'Circle' creates an error
    def area(self):
        return 3.14 * self.radius * self.radius


# 3. Usage
# s = Shape() # Error: Can't instantiate abstract class
c = Circle(5)
print(f"Area: {c.area()}")
# Topic of the Day: Intro to OOP (Classes & Objects)
# Explanation: Think of a Class as a "Blueprint" or a "Cookie Cutter." It defines the shape. Think of an Object as the actual "House" built from the blueprint or the "Cookie" made from the cutter.
# class: Defines the blueprint.
# __init__: The constructor. It runs automatically when you create a new object to set it up.
# self: Refers to this specific object (e.g., this specific cookie, not all cookies).

# 1. The Blueprint (Class)
class Dog:
    # The Constructor
    def __init__(self, name, breed):
        self.name = name   # Attribute
        self.breed = breed # Attribute

    # A Method (Action)
    def bark(self):
        return f"{self.name} says Woof!"

# 2. Creating Objects (Instances)
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Rex", "German Shepherd")

# 3. Using the Objects
print(dog1.bark()) # Output: Buddy says Woof!
print(dog2.breed)  # Output: German Shepherd
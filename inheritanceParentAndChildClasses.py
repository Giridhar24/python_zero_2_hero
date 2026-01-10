# Topic of the Day: Inheritance (Parent & Child Classes)
# Explanation: Inheritance allows a "Child" class to steal (inherit) all the features of a "Parent" class.
# You only write the shared code once in the Parent, and all Children get it automatically. This is key for code reuse.

# 1. The Parent Class (General)
class Animal:
    def speak(self):
        print("Some generic animal sound")

# 2. The Child Class (Specific)
# We put (Animal) in parentheses to inherit from it
class Cat(Animal):
    # We can 'Override' the parent's method with a specific version
    def speak(self):
        print("Meow!")

class Dog(Animal):
    def speak(self):
        print("Woof!")

# 3. Usage
generic_creature = Animal()
kitty = Cat()

generic_creature.speak() # Output: Some generic animal sound
kitty.speak()            # Output: Meow! (It used its own version)
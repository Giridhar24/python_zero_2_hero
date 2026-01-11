# Topic of the Day: Polymorphism
# Explanation: Polymorphism means "Many Forms."
# It allows you to use a single interface (method name) to handle different types of objects.
# You don't need to know what exact class an object is, only that it has the method you want to call.

class Bird:
    def fly(self):
        return "Flap flap!"

class Airplane:
    def fly(self):
        return "Engines roaring!"

class Fish:
    def swim(self):
        return "Splash!"

# A function that expects ANYTHING that can fly
def lift_off(flying_object):
    # This works regardless of whether it's a Bird or Plane
    # This is Polymorphism in action
    print(flying_object.fly())

# Creating objects
bird = Bird()
plane = Airplane()
fish = Fish()

lift_off(bird)   # Output: Flap flap!
lift_off(plane)  # Output: Engines roaring!

# lift_off(fish)
# ERROR: Fish object has no attribute 'fly'.
# Python checks at runtime (Duck Typing: "If it walks like a duck...")a
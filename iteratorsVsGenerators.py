# Topic of the Day: Iterators vs. Generators (Deep Dive)
#
# Explanation: We used yield before. But what is happening under the hood?
#
# Iterable: Anything you can loop over (List, String). It has an __iter__ method.
#
# Iterator: The object that actually fetches the next item. It has a __next__ method.
#
# Generator: A shortcut to create Iterators using yield.


# 1. Manual Iterator Class (The Hard Way)
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration # Signals the loop to stop

# 2. Generator (The Easy Way)
def counter_gen(limit):
    current = 0
    while current < limit:
        current += 1
        yield current

# Both work identically in a loop
print("--- Class Iterator ---")
for num in Counter(3):
    print(num)

print("--- Generator Function ---")
for num in counter_gen(3):
    print(num)
# Topic of the Day: Context Managers (with statement)
# Explanation: You use with open(...) to handle files.
# But how does it work? It uses the Context Manager protocol.
# You can build your own to manage resources (like database connections) automatically.
# It guarantees that "cleanup" code runs even if the program crashes.
# Required Methods: __enter__ (Setup) and __exit__ (Cleanup).

class Timer:
    def __enter__(self):
        print("--- Timer Started ---")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("--- Timer Stopped ---")
        # Returning False propagates errors; True suppresses them
        return False

# Usage
print("Before context")

with Timer():
    print("Inside the block: Doing work...")
    # Even if I crash here, __exit__ will still run!

print("After context")
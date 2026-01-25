# Topic of the Day: Unit Testing (unittest)
# Explanation: How do you know your code actually works? You write code to test your code.
# unittest is Python's built-in library for this.
# It runs your functions with specific inputs and checks if the output matches what you expect.

import unittest


# 1. The Function to Test
def add(a, b):
    return a + b


# 2. The Test Class
class TestMathOperations(unittest.TestCase):

    # Test 1: Standard case
    def test_add_integers(self):
        self.assertEqual(add(2, 3), 5)

    # Test 2: Edge case (negatives)
    def test_add_negatives(self):
        self.assertEqual(add(-1, -1), -2)

    # Test 3: Failure case (Intentionally checking wrong logic)
    # This will fail if we run it, proving the test works.
    # def test_fail(self):
    #     self.assertEqual(add(2, 2), 5)


# 3. Run the tests
if __name__ == '__main__':
    unittest.main()
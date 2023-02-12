import unittest
from solution_20_valid_parentheses import Solution

class MyTestCase(unittest.TestCase):
    def test_example1(self):
        s = "()"
        expected = True
        solution = Solution()
        self.assertEqual(expected, solution.isValid(s))

class MyTestCase(unittest.TestCase):
    def test_example2(self):
        s = "()[]{}"
        expected = True
        solution = Solution()
        self.assertEqual(expected, solution.isValid(s))

class MyTestCase(unittest.TestCase):
    def test_example3(self):
        s = "(]"
        expected = False
        solution = Solution()
        self.assertEqual(expected, solution.isValid(s))

class MyTestCase(unittest.TestCase):
    def test_example87(self):
        s = ")(){}"
        expected = False
        solution = Solution()
        self.assertEqual(expected, solution.isValid(s))

class MyTestCase(unittest.TestCase):
    def test_example89(self):
        s = "){"
        expected = False
        solution = Solution()
        self.assertEqual(expected, solution.isValid(s))

if __name__ == '__main__':
    unittest.main()

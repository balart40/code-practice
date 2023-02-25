import unittest
from solution_9_palindrome_number import Solution

class MyTestCase(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        x = 121
        expected = True
        self.assertEqual(expected, solution.isPalindrome(x))

    def test_example2(self):
        solution = Solution()
        x = -121
        expected = False
        self.assertEqual(expected, solution.isPalindrome(x))

    def test_example3(self):
        solution = Solution()
        x = 10
        expected = False
        self.assertEqual(expected, solution.isPalindrome(x))


if __name__ == '__main__':
    unittest.main()

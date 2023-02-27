import unittest
from solution_1328_break_a_palindrome import Solution

class MyTestCase(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        palindrome = "abccba"
        expected = "aaccba"
        self.assertEqual(expected, solution.breakPalindrome(palindrome))

    def test_example2(self):
        solution = Solution()
        palindrome = "a"
        expected = ""
        self.assertEqual(expected, solution.breakPalindrome(palindrome))

if __name__ == '__main__':
    unittest.main()


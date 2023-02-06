import unittest
from solution_162_valid_palindrome import Solution


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        s = "A man, a plan, a canal: Panama"
        expected = True
        self.assertEqual(expected, solution.isPalindrome(s))

    def test_example2(self):
        solution = Solution()
        s = "race a car"
        expected = False
        self.assertEqual(expected, solution.isPalindrome(s))

    def test_example3(self):
        solution = Solution()
        s = " "
        expected = True
        self.assertEqual(expected, solution.isPalindrome(s))

if __name__ == '__main__':
    unittest.main()

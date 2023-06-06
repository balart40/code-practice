import unittest
from solution_longest_parenthesis_subarray import Solution


class MyTestCase(unittest.TestCase):
    def test_example3(self):
        s = "((()))())()()"
        expected = 8
        solution = Solution()
        self.assertEqual(expected, solution.longestValidParentheses(s))

if __name__ == '__main__':
    unittest.main()

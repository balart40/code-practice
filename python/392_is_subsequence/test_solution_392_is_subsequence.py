import unittest
from solution_392_is_subsequence import Solution


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        s = "abc"
        t = "ahbgdc"
        expected = True
        self.assertEqual(expected, solution.isSubsequence(s, t))

    def test_example2(self):
        solution = Solution()
        s = "axc"
        t = "ahbgdc"
        expected = False
        self.assertEqual(expected, solution.isSubsequence(s, t))

    def test_example14(self):
        solution = Solution()
        s = "acb"
        t = "ahbgdc"
        expected = False
        self.assertEqual(expected, solution.isSubsequence(s, t))


if __name__ == '__main__':
    unittest.main()

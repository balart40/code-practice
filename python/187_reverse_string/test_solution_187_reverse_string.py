import unittest
from solution_187_reverse_string import Solution


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        s = ["h","e","l","l","o"]
        expected = ["o","l","l","e","h"]
        self.assertEqual(expected, solution.reverseString(s))

class MyTestCase(unittest.TestCase):
    def test_example2(self):
        solution = Solution()
        s = ["H","a","n","n","a","h"]
        expected = ["h","a","n","n","a","H"]
        self.assertEqual(expected, solution.reverseString(s))

if __name__ == '__main__':
    unittest.main()

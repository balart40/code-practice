import unittest
from solution_8_string_to_integer_atoi import Solution


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        s = "42"
        solution = Solution()
        expected = 42
        self.assertEqual(expected, solution.myAtoi(s))

    def test_example2(self):
        s = "   -42"
        solution = Solution()
        expected = -42
        self.assertEqual(expected, solution.myAtoi(s))

    def test_example3(self):
        s = "4193 with words"
        solution = Solution()
        expected = 4193
        self.assertEqual(expected, solution.myAtoi(s))

    def test_example5(self):
        s = "3.14159"
        solution = Solution()
        expected = 3
        self.assertEqual(expected, solution.myAtoi(s))


if __name__ == '__main__':
    unittest.main()

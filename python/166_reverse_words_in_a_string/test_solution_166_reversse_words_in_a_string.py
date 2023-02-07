import unittest
from solution_166_reverse_words_in_a_string import Solution

class MyTestCase(unittest.TestCase):
    def test_exmple1(self):
        solution = Solution()
        s = "the sky is blue"
        expected = "blue is sky the"
        self.assertEqual(expected, solution.reverseWords(s))

    def test_exmple2(self):
        solution = Solution()
        s = "  hello world  "
        expected = "world hello"
        self.assertEqual(expected, solution.reverseWords(s))

    def test_exmple3(self):
        solution = Solution()
        s = "a good   example"
        expected = "example good a"
        self.assertEqual(expected, solution.reverseWords(s))


if __name__ == '__main__':
    unittest.main()

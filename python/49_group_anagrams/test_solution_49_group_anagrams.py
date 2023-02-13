import unittest
from solution_49_group_anagrams import Solution


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']]
        self.assertEqual(expected, solution.groupAnagrams(strs))


class MyTestCase(unittest.TestCase):
    def test_example2(self):
        solution = Solution()
        strs = [""]
        expected = [[""]]
        self.assertEqual(expected, solution.groupAnagrams(strs))


class MyTestCase(unittest.TestCase):
    def test_example2(self):
        solution = Solution()
        strs = ["a"]
        expected = [["a"]]
        self.assertEqual(expected, solution.groupAnagrams(strs))


if __name__ == '__main__':
    unittest.main()

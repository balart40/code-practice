import unittest
from solution_56_merge_intervals import Solution


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(expected, solution.merge(intervals))


class MyTestCase(unittest.TestCase):
    def test_example2(self):
        solution = Solution()
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]
        self.assertEqual(expected, solution.merge(intervals))

class MyTestCase(unittest.TestCase):
    def test_example46(self):
        solution = Solution()
        intervals = [[1, 4], [2, 3]]
        expected = [[1, 4]]
        self.assertEqual(expected, solution.merge(intervals))

class MyTestCase(unittest.TestCase):
    def test_example48(self):
        solution = Solution()
        intervals = [[1,4],[0,2],[3,5]]
        expected = [[0,5]]
        self.assertEqual(expected, solution.merge(intervals))

if __name__ == '__main__':
    unittest.main()

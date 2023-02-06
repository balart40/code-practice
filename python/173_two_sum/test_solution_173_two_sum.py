import unittest
from solution_173_two_sum import Solution

class MyTestCase(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertEqual(expected, solution.twoSum(nums, target), "IDXs of target sum does not match")

class MyTestCase(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        self.assertEqual(expected, solution.twoSum(nums, target), "IDXs of target sum does not match")

class MyTestCase(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        self.assertEqual(expected, solution.twoSum(nums, target), "IDXs of target sum does not match")

if __name__ == '__main__':
    unittest.main()

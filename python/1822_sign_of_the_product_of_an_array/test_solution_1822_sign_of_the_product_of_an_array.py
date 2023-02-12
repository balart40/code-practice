import unittest
from solution_1822_sign_of_the_product_of_an_array import Solution

class MyTestCase(unittest.TestCase):
    def test_example1(self):
        nums = [-1,-2,-3,-4,3,2,1]
        expected = 1
        solution = Solution()
        self.assertEqual(expected, solution.arraySign(nums))

class MyTestCase(unittest.TestCase):
    def test_example2(self):
        nums = [1,5,0,2,-3]
        expected = 0
        solution = Solution()
        self.assertEqual(expected, solution.arraySign(nums))

class MyTestCase(unittest.TestCase):
    def test_example3(self):
        nums = [-1,1,-1,1,-1]
        expected = -1
        solution = Solution()
        self.assertEqual(expected, solution.arraySign(nums))

if __name__ == '__main__':
    unittest.main()

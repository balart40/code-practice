import unittest


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        from solution_977_squares_of_sorted_array import Solution
        solution = Solution()
        nums = [-4, -1, 0, 3, 10]
        expected = [0, 1, 9, 16, 100]
        self.assertEqual(expected, solution.sortedSquares(nums))


def test_example2(self):
    from solution_977_squares_of_sorted_array import Solution
    solution = Solution()
    nums = [-7, -3, 2, 3, 11]
    expected = [4, 9, 9, 49, 121]
    self.assertEqual(expected, solution.sortedSquares(nums))


if __name__ == '__main__':
    unittest.main()

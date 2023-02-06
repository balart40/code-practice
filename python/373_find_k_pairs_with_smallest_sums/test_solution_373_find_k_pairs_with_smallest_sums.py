import unittest
from solution_373_find_k_pairs_with_smallest_sums import Solution


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        nums1 = [1, 7, 11]
        nums2 = [2, 4, 6]
        expected = [[1, 2], [1, 4], [1, 6]]
        k = 3
        solution = Solution()
        self.assertEqual(expected, solution.kSmallestPairs(nums1, nums2, k))

    def test_example2(self):
        nums1 = [1, 1, 2]
        nums2 = [1, 2, 3]
        expected = [[1, 1], [1, 1]]
        k = 2
        solution = Solution()
        self.assertEqual(expected, solution.kSmallestPairs(nums1, nums2, k))

    def test_example3(self):
        nums1 = [1, 2]
        nums2 = [3]
        expected = [[1, 3], [2, 3]]
        k = 3
        solution = Solution()
        self.assertEqual(expected, solution.kSmallestPairs(nums1, nums2, k))

    def test_example15(self):
        nums1 = [1, 2, 4, 5, 6]
        nums2 = [3, 5, 7, 9]
        expected = [[1, 3], [2, 3], [1, 5]]
        k = 3
        solution = Solution()
        self.assertEqual(expected, solution.kSmallestPairs(nums1, nums2, k))

if __name__ == '__main__':
    unittest.main()

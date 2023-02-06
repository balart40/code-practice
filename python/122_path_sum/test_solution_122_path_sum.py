import unittest
from solution_122_path_sum import Solution, TreeNode


class MyTestCase(unittest.TestCase):
    def test_three_nodes(self):
        leftNode = TreeNode(2)
        rightNode = TreeNode(3)
        root = TreeNode(1, leftNode, rightNode)
        expectedResult = False
        targetSum = 5
        solution = Solution()
        self.assertEqual(expectedResult, solution.hasPathSum(root, targetSum), "Expected Sum = 6")

    def test_nine_nodes(self):
        one = TreeNode(7)
        two = TreeNode(2)
        three = TreeNode(11, one, two)
        four = TreeNode(4, three)
        five = TreeNode(1)
        six = TreeNode(4, None, five)
        seven = TreeNode(13)
        eight = TreeNode(8, seven, six)
        root = TreeNode(5, four, eight)
        expectedResult = True
        targetSum = 22
        solution = Solution()
        self.assertEqual(expectedResult, solution.hasPathSum(root, targetSum), "Expected Sum = 22 to be true")

if __name__ == '__main__':
    unittest.main()

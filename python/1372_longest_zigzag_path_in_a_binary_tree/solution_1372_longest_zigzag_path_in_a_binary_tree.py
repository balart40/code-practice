# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def longestZigZagDfs(node, isRight, curr_length):
            if node ==  None:
                return curr_length - 1
            leftLeft = leftRight = rightRight = rightLeft = curr_length
            if (isRight):
                # if direction was right and keep going right then reset
                rightRight = longestZigZagDfs(node.right, isRight, 1)
                # if direction was right and then we go left add
                rightLeft = longestZigZagDfs(node.left, not isRight, curr_length + 1)
            else:
                # if direction was left and keep going left reset
                leftLeft = longestZigZagDfs(node.left, isRight ,1)
                # if direction was left and then we go right add
                leftRight = longestZigZagDfs(node.right, not isRight, curr_length + 1)
            return max(leftLeft, leftRight, rightLeft, rightRight)

        return max(longestZigZagDfs(root, True, 0), longestZigZagDfs(root, False, 0))
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_depth = 0

        def max_depth_rec(node, curr_max_depth):
            if node == None:
                return curr_max_depth - 1
            left = max_depth_rec(node.left, curr_max_depth +1)
            right = max_depth_rec(node.right, curr_max_depth +1)
            return max(left, right)

        return max_depth_rec(root, 1)
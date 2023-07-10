# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_level = 10**5
        def minDepthRec(node, level):
            if node == None:
                return level - 1
            elif node.left == None and node.right == None:
                return level
            left = minDepthRec(node.left, level + 1) if node.left else min_level
            right = minDepthRec(node.right, level + 1) if node.right else min_level
            return min(left, right)
        return minDepthRec(root, 1)
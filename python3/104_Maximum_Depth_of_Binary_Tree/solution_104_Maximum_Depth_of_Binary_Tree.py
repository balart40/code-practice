# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def dfs_rec(node, depth):
            if not node: return depth
            left = dfs_rec(node.left, depth + 1) if node.left else depth
            right = dfs_rec(node.right, depth + 1) if node.right else depth
            return max(left, right)
        return dfs_rec(root, 1)
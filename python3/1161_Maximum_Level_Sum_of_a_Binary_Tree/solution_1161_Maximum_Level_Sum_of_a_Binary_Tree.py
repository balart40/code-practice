# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_d = collections.defaultdict(int)
        def max_level_sum_rec(node, level):
            nonlocal level_d
            level_d[level] += node.val
            if node.left:
                max_level_sum_rec(node.left, level + 1)
            if node.right:
                max_level_sum_rec(node.right, level + 1)
            return
        max_level_sum_rec(root, 1)
        return max(level_d, key=level_d.get)
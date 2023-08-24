# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        longest_path = 0
        def dfs_rec(node, right, curr_path_length):
            nonlocal longest_path
            if not node:
                return curr_path_length - 1
            longest_path = max(longest_path, curr_path_length)
            if right:
                # if direction is right and we have a right node rightright
                dfs_rec(node.right, right, 1)
                # right left
                dfs_rec(node.left, not right, curr_path_length + 1)
            if not right:
                dfs_rec(node.left, right, 1)
                dfs_rec(node.right, not right, curr_path_length + 1)
            return
        dfs_rec(root, True, 0)
        dfs_rec(root, False, 0)
        return longest_path
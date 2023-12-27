# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def traversal_rec(node, result):
            if not node:
                result.append(None)
                return
            result.append(node.val)
            traversal_rec(node.left, result)
            traversal_rec(node.right, result)
            return result
        left, right = [] , []
        left = traversal_rec(p, left)
        right = traversal_rec(q, right)
        return True if left == right else False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def goodNodes_rec(node, observed):
            nonlocal count
            if not node:
                return
            if node.val >= observed:
                count += 1
                observed = node.val
            if node.left:
                goodNodes_rec(node.left, observed)
            if node.right:
                goodNodes_rec(node.right, observed)
            return

        goodNodes_rec(root, root.val)
        return count

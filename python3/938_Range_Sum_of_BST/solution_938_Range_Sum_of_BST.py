# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def rangeSumBstRec(node, low, high):
            if not node: return 0
            current = 0
            if node.val >= low and node.val <= high:
                current += node.val
            left = rangeSumBstRec(node.left, low, high)
            right = rangeSumBstRec(node.right, low, high)
            return current + left + right
        return rangeSumBstRec(root, low, high)
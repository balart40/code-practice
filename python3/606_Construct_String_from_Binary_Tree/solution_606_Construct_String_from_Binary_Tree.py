# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def pre_order_rec(node):
            if not node: return
            result = str(node.val)
            if node.left:
                result += "(" + pre_order_rec(node.left) + ")"
            if node.right:
                if not node.left: result += "()"
                result += "(" + pre_order_rec(node.right) + ")"
            return result
        return pre_order_rec(root)
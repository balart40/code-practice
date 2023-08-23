# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_nodes_one = []
        leaf_nodes_two = []
        def in_order_rec(node, lst):
            if not node:
                return
            if not node.left and not node.right:
                lst.append(node.val)
                return
            if node.left:
                in_order_rec(node.left, lst)
            if node.right:
                in_order_rec(node.right, lst)
            return
        in_order_rec(root1,leaf_nodes_one)
        in_order_rec(root2,leaf_nodes_two)
        return leaf_nodes_one == leaf_nodes_two
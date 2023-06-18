# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        def recursive_traversal(node, val):
            if node == None:
                return None
            if node.val == val:
                return node
            left = recursive_traversal(node.left, val)
            right = recursive_traversal(node.right, val)
            return left if left else right if right else None

        return recursive_traversal(root, val)
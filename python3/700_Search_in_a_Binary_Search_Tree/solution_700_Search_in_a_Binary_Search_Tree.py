# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        result =  None
        def search_bst_rec(node):
            nonlocal val
            nonlocal result
            if not node:
                return
            else:
                if node.val == val:
                    result = node
                    return
                search_bst_rec(node.left)
                search_bst_rec(node.right)
                return
        search_bst_rec(root)
        return result
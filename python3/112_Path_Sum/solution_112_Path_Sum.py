# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        result = False
        def hasPathSumRec(node, currSum):
            nonlocal result
            nonlocal targetSum
            if not node: return
            currSum += node.val
            if not node.left and not node.right and currSum == targetSum:
                result = True
                return
            hasPathSumRec(node.right, currSum)
            hasPathSumRec(node.left, currSum)
            return

        hasPathSumRec(root, 0)
        return result
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :rtype: int
        """
        def hasPathSumRecursive(root, rootVal, targetSum):
            if root.left is None and root.right is None:
                return rootVal == targetSum
            L = False
            R = False
            if root.left is not None:
                L = hasPathSumRecursive(root.left, rootVal + root.left.val, targetSum)
            if root.right is not None:
                R = hasPathSumRecursive(root.right, rootVal + root.right.val, targetSum)
            return True if L or R else False

        return hasPathSumRecursive(root, root.val, targetSum)
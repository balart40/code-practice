# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def preOrder(node, minRange, maxRange):
            # continue
            if minRange < node.val < maxRange:
                # leaf
                C = True
                L = True
                R = True
                if node.left == None and node.right == None:
                    C = True
                if node.left != None:
                    L =  preOrder(node.left, minRange, node.val)
                if node.right != None:
                    R =  preOrder(node.right, node.val, maxRange)
                return C and L and R
            else:
                return False

        initialMaxRange = 9223372036854775807
        initialMinRange = -9223372036854775806
        return preOrder(root, initialMinRange, initialMaxRange)
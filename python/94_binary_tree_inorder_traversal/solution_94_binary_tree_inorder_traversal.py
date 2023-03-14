# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inOrderRec(node, traverselst):
            if node.left != None:
                inOrderRec(node.left, traverselst)
            traverselst.append(node.val)
            if node.right != None:
                inOrderRec(node.right, traverselst)
            return

        traverseList = []
        if root != None:
            inOrderRec(root, traverseList)
        return traverseList
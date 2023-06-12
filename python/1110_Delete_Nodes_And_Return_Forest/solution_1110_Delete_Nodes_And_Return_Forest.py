# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        result = []

        def delNodesRec(node, to_delete):
            if node == None:
                return None
            node.left = delNodesRec(node.left, to_delete)
            node.right = delNodesRec(node.right, to_delete)
            if node.val in to_delete:
                if node.left:
                    result.append(node.left)
                if node.right:
                    result.append(node.right)
                return None
            return node

        delNodesRec(root, to_delete)
        if root.val not in to_delete:
            result.append(root)
        return result
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def goodNodesRec(node, maxx):
            # am i a good node?
            amImGoodNode = 1 if node.val >= maxx else 0
            # store so far maxx
            maxx = node.val if node.val >= maxx else maxx
            left = right = 0
            if node.left != None:
                left = goodNodesRec(node.left, maxx)
            if node.right != None:
                right = goodNodesRec(node.right, maxx)
            return amImGoodNode + left +right

        seen = set()
        seen.add(root.val)
        return goodNodesRec(root, root.val)
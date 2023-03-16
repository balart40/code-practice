# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def levelOrderRec(node, level, lst):
            if node != None:
                if len(lst) == level:
                    lst.append([])
                lst[level].append(node.val)
                if node.left != None:
                    levelOrderRec(node.left, level+1, lst)
                if node.right != None:
                    levelOrderRec(node.right, level+1, lst)
        lst = []
        levelOrderRec(root, 0, lst)
        return lst

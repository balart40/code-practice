# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d = dict()

        def in_order_traversal(node, level):
            if node == None:
                return
            if level not in d:
                d[level] = [node.val]
            else:
                d[level].append(node.val)
            in_order_traversal(node.left, level + 1)
            in_order_traversal(node.right, level + 1)
            return

        result = []

        in_order_traversal(root, 0)

        for key, value in d.items():
            result.append(d[key][-1])

        return result
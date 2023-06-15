# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d = dict()
        result = []
        def in_order_traversal(node, level):
            if not node:
                return
            in_order_traversal(node.left, level+1)
            if level not in d:
                d[level] = [node.val]
            else:
                d[level].append(node.val)
            in_order_traversal(node.right, level +1)
            return

        in_order_traversal(root, 1)

        max_sum = root.val
        level = 1
        for key, val in d.items():
            curr_summ = sum(val)
            if curr_summ > max_sum:
                max_sum = curr_summ
                level = key
        return level


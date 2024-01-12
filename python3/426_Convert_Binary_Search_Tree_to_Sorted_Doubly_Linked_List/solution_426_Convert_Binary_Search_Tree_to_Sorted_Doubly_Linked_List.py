"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        ordered_list = []

        def in_order_rec(node):
            nonlocal ordered_list
            if not node: return
            in_order_rec(node.left)
            ordered_list.append(node)
            in_order_rec(node.right)
            return

        in_order_rec(root)

        n = len(ordered_list)
        first = curr = ordered_list[0]

        for i in range(n):
            ordered_list[i].left = ordered_list[i - 1]
            ordered_list[i].right = ordered_list[(i+1) % n]

        return first
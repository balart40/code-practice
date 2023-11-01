# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d = collections.defaultdict(int)
        self.max_node = - 1 * 10 ** 5
        self.count = 0
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def in_order_rec(node):
            if not node: return
            self.d[node.val] += 1
            if self.d[node.val] >= self.count:
                self.max_node = node.val
                self.count = self.d[node.val]
            in_order_rec(node.left)
            in_order_rec(node.right)
            return
        in_order_rec(root)
        return [k for k in self.d if self.d[k] == self.count]
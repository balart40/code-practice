# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels_d = collections.defaultdict()
        result = []
        def pre_order(node, level):
            nonlocal levels_d
            if not node: return
            if level not in levels_d:
                levels_d[level] = []
            levels_d[level].append(node.val)
            pre_order(node.left, level + 1)
            pre_order(node.right, level + 1)
        pre_order(root, 1)
        for level in levels_d:
            result.append(levels_d[level][-1])
        return result
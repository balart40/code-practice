# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels_dict = collections.defaultdict(list)
        def traversal_rec(node, level):
            nonlocal levels_dict
            if not node: return
            levels_dict[level].append(node.val) if level % 2 != 0 else levels_dict[level].insert(0, node.val)
            traversal_rec(node.right, level + 1)
            traversal_rec(node.left, level + 1)
            return

        traversal_rec(root, 0)
        return levels_dict.values()
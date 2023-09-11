# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        d = collections.defaultdict(list)
        min_idx, max_idx = 0, 0
        queue = collections.deque()
        queue.append((root, 0))
        while queue:
            node, vertical_idx = queue.popleft()
            min_idx = min(min_idx, vertical_idx)
            max_idx = max(max_idx, vertical_idx)
            d[vertical_idx].append(node.val)
            if node.left: queue.append((node.left, vertical_idx - 1))
            if node.right: queue.append((node.right, vertical_idx + 1))

        return [d[key] for key in range(min_idx, max_idx +1)]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        prefix_sum = collections.defaultdict(int)
        prefix_sum[0] = 1
        def path_sum_rec(node, curr_sum):
            nonlocal count
            if not node: return
            local_sum = curr_sum + node.val
            if local_sum - targetSum in prefix_sum:
                count += prefix_sum[local_sum - targetSum]
            if local_sum not in prefix_sum:
                prefix_sum[local_sum] = 1
            else:
                prefix_sum[local_sum] += 1
            path_sum_rec(node.left, local_sum)
            path_sum_rec(node.right, local_sum)
            prefix_sum[local_sum] -= 1
            if prefix_sum[local_sum] == 0:
                del[prefix_sum[local_sum]]
            return

        path_sum_rec(root, 0)
        return count
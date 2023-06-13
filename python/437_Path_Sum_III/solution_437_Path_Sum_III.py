# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        counter = []
        counter.append(0)

        def pathSumRec(node, curr_path, current_sum):
            if node == None:
                return
            current_sum += node.val
            temp_sum = current_sum
            if current_sum == targetSum:
                counter[0] += 1
            for num in curr_path:
                temp_sum -= num
                if temp_sum == targetSum:
                    counter[0] += 1
            curr_path.append(node.val)
            pathSumRec(node.left, curr_path, current_sum)
            pathSumRec(node.right, curr_path, current_sum)
            curr_path.pop()

        pathSumRec(root, [], 0)
        return counter[0]

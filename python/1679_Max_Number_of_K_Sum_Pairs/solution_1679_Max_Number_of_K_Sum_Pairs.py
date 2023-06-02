class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        d = dict()
        for i in range(len(nums)):
            target  = k - nums[i]
            if target in d and d[target] > 0:
                count += 1
                d[target] -= 1
            elif nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]]  += 1
        return count
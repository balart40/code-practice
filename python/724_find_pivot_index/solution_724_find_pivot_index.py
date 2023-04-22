class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Get sum of all
        totalSum = 0
        for i in range(n):
            totalSum += nums[i]
        left = 0
        for i in range(n):
            currRight = totalSum - left - nums[i]
            if left == currRight:
                return i
            left += nums[i]
        return -1

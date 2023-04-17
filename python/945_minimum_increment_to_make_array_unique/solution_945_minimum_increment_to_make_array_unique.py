class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = sorted(nums)
        count = 0
        for i in range(1,n):
            if nums[i] <= nums[i-1]:
                count += nums[i-1]+1 - nums[i]
                nums[i]=nums[i-1]+1
        return count

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        n = len(nums)
        if n == 1:
            return False
        for i in range(1,n):
            if nums[i] == nums[i - 1]:
                return True
        return False
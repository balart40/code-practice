class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        nums.sort()
        for i in range(0, n):
            if i == 0 and nums[i] != nums[i + 1]:
                return nums[i]
            elif i == n - 1 and nums[i] != nums[i - 1]:
                return nums[i]
            else:
                if nums[i-1] != nums[i] != nums[i + 1]:
                    return nums[i]
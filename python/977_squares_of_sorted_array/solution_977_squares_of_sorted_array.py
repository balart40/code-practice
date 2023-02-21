class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 1:
            nums[0] = nums[0]*nums[0]
        else:
            if nums[0] < 0:
                nums.sort(key=lambda x: abs(x))
            for i in range(n):
                nums[i] = nums[i]*nums[i]
        return nums

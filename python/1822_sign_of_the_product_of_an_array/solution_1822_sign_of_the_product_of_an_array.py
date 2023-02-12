class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negativesFound = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                negativesFound += 1
            elif nums[i] == 0:
                return 0
        if negativesFound % 2 is not 0:
            return -1
        else:
            return 1

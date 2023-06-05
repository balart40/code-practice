class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = left = 0
        n = len(nums)
        k = 1
        for right in range(n):
            if nums[right] == 0:
                if k == 0:
                    while nums[left] != 0:
                        left += 1
                    left += 1
                else:
                    k -= 1
            result = max(result, right - left)
        return result
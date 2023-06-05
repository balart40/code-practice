class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = left = 0
        n = len(nums)
        for right in range(n):
            # if we  a
            if nums[right] == 0:
                # we run out of zeros
                if k == 0:
                    while nums[left] != 0:
                        left += 1
                    left += 1
                else:
                    k -= 1
            result = max(result, right - left + 1)
        return result
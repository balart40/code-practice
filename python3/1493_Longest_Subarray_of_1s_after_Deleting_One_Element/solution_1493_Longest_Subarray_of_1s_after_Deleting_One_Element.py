class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = 0
        k = 1
        n = len(nums)
        while right < n:
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            right += 1
        return right - left - 1
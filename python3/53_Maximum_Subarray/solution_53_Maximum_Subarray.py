class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        max_sum = float('-inf')
        for num in nums:
            temp += num
            max_sum = max(temp, max_sum)
            temp = 0 if temp <0 else temp
        return max_sum
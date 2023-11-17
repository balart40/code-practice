class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = neg = 0
        seen = set()
        for num in nums:
            if num != 0:
                if num < 0: neg += 1
                else: pos += 1
        return max(pos,neg)
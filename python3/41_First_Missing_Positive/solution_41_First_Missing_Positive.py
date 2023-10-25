class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        unique_nums_set = set(nums)
        i = 1
        while i in unique_nums_set:
            i += 1
        return i
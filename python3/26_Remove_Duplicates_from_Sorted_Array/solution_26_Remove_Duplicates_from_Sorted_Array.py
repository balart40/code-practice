class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = len(nums) - 2
        while(i > -1):
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
            i -= 1
        return len(nums)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        n = len(nums)
        for i in range(n):
            pivot_val = nums[i]
            right -= pivot_val
            if right == left:
                return i
            left += pivot_val
        return -1
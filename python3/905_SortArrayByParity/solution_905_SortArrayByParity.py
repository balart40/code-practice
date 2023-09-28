class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] % 2 != 0:
                odd.append(nums.pop(i))
        return nums + odd

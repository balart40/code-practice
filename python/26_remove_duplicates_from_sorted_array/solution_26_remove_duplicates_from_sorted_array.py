class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 1
        idxToRemove = []
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                idxToRemove.insert(0, i)
        result = len(nums) - len(idxToRemove)
        for idx in idxToRemove:
            nums.pop(idx)
            nums.append(0)
        return result

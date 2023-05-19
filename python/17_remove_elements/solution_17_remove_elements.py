class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        indexes_to_remove = []
        for i in range(n-1,-1,-1):
            if nums[i] == val:
                indexes_to_remove.append(i)
        m = len(indexes_to_remove)
        for j in range(m):
            nums.pop(indexes_to_remove[j])
            nums.append(None)
        print nums
        return n - m
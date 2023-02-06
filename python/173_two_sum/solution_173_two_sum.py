class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicto = dict()
        for i in range(len(nums)):
            lookFor = target - nums[i]
            found = dicto.get(lookFor, None)
            if found is not None:
                return [found, i]
            else:
                dicto[nums[i]] = i

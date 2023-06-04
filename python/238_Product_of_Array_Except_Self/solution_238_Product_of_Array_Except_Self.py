class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        all_multiplied = 1
        zeros = nums.count(0)
        result = [0]*len(nums)
        if zeros > 1:
            return result
        else:
            for i in range(len(nums)):
                if nums[i] != 0:
                    all_multiplied *= nums[i]
            if zeros == 1:
                idx = nums.index(0)
                result[idx] = all_multiplied
            else:
                for i in range(len(nums)):
                    result[i] =  all_multiplied/ nums[i]
        return result

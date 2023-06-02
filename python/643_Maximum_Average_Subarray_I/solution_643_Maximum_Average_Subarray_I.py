class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        max_sum = curr_sum = sum(nums[0:k])
        for i in range(0, n - k):
            curr_sum = curr_sum - nums[i] + nums[i + k]
            max_sum = max(max_sum, curr_sum)
        return max_sum/float(k)

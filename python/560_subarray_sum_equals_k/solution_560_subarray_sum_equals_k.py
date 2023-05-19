class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        # this solution only works with positive numbers
        left = 0
        right = 1
        counter = 0
        n = len(nums)
        if n ==  1 and nums[0] != k:
            return 0
        if n ==  1 and nums[0] == k:
            return nums[0]
        while left <= right and right < n:
            summation = sum(nums[left:right+1])
            if summation  == k:
                counter += 1
                right += 1
            elif summation < k:
                right += 1
            else:
                left += 1
        return counter
        """
        # hash map
        dicto = dict()
        # freq sum  == 0 -> 1
        dicto[0] = 1
        curr_sum = counter = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum - k in dicto:
                # add frequencies of sum
                counter += dicto[curr_sum - k]
            if curr_sum in dicto:
                dicto[curr_sum] += 1
            else:
                dicto[curr_sum] = 1
        return counter

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        d = dict()
        d[0] = 1
        curr_sum = counter = 0
        for i in range(n):
            curr_sum += nums[i]
            remainder = curr_sum % k
            # remainder negative
            if remainder < 0:
                remainder += k
            if remainder in d:
                counter += d[remainder]
                d[remainder] += 1
            else:
                d[remainder] = 1
        return counter

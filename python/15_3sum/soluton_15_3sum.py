class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums = sorted(nums)

        result = []
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            a = nums[i]
            # two sum
            left = i+1
            right = n - 1
            while left < right:
                currSum = a + nums[left] + nums[right]
                if currSum > 0:
                    right -= 1
                elif currSum < 0:
                    left += 1
                else:
                    b = nums[left]
                    c = nums[right]
                    result.append([a,b,c])
                    left += 1
                    while nums[left]==nums[left-1] and left < right:
                        left += 1
        return result

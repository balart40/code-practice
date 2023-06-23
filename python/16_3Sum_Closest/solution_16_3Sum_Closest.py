class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        result = sum(nums[:3])
        diff = 10**4
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # two sum
            left = i + 1
            right = n - 1
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                curr_diff = abs(currSum - target)
                if not curr_diff:
                    return currSum
                if curr_diff < diff:
                    result = currSum
                    diff = curr_diff
                if currSum < target:
                    left += 1
                else:
                    right -= 1
        return result
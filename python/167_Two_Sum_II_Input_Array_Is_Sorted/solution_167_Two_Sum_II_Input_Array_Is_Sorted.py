class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        left = 0
        right = n -1
        while left < right:
            currSumm = numbers[left] + numbers[right]
            if currSumm > target:
                right -= 1
            elif currSumm < target:
                left += 1
            else:
                return [left+1, right+1]
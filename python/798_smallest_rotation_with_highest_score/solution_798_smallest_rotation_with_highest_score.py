class Solution(object):
    def bestRotation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums2 = [i for i in range(n)]

        heapRotations = []
        for i in range(n):
            if i != 0:
                first = nums.pop(0)
                nums.append(first)
            heapRotations.append([i, sum([1 if i[0]<=i[1] else 0 for i in zip(nums, nums2)])])

        heapq.heapify(heapRotations)
        res = heapq.nlargest(1,heapRotations, key=lambda x : x[1])[0][0]
        return res
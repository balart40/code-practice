class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        #Solution 1
        """
        heap =  []
        n = len(nums)
        for i in range(n):
            heapq.heappush(heap, nums[i])
        
        kItems = heapq.nlargest(k,nums)
        kItem = kItems[-1]
        return kItem
        """

        #Solution 2 two liner
        heapq.heapify(nums)
        return heapq.nlargest(k,nums)[-1]
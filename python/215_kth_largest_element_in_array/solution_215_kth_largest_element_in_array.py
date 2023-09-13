class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # ***** SOLUTION 1 *****
        # nums.sort()
        # nums = nums[::-1]
        # return nums[k-1]
        # Solution 2 *****
        # **** SOLUTION 2
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
        #heapq.heapify(nums)
        #return heapq.nlargest(k,nums)[-1]
        # Solution 3
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
        return heapq.nlargest(k, heap)[-1]
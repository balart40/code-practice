class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # ***** SOLUTION 1 *****
        # nums.sort()
        # nums = nums[::-1]
        # return nums[k-1]
        # Solution 2 *****
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        return heapq.nlargest(k, heap)[-1]
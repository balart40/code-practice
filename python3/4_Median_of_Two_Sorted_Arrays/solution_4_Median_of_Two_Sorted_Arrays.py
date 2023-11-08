class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        heap = list(heapq.merge(nums1, nums2))
        n = len(heap)
        return (heap[n//2-1] + heap[n//2])/2.0 if n % 2 == 0 else heap[n//2]
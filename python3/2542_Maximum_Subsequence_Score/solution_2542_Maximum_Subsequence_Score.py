class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(x[0], x[1]) for x in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda p : p[1], reverse=True)
        p_sum, result = 0, 0
        heap =[]
        for p1,p2 in pairs:
            p_sum += p1
            heapq.heappush(heap, p1)
            if len(heap) == k:
                result = max(result, p_sum*p2)
                p_sum -= heapq.heappop(heap)
        return result
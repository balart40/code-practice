class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.defaultdict(int)
        for num in nums:
            d[num]+= 1
        heap = []
        for key in d:
            heapq.heappush(heap, (d[key], key))
        return [val[1] for val in heapq.nlargest(k, heap)]
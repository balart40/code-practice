class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = collections.defaultdict(int)
        for num in arr:
            d[num] += 1
        return len(d.keys()) == len(set(d.values()))
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = collections.defaultdict(lambda: 0)
        n = len(arr)
        for i in range(n):
            d[arr[i]] += 1
        return len(set(arr)) == len(set(d.values()))
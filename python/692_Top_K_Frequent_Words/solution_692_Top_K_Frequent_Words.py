class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        n = len(words)
        d = dict()
        result = []

        for i in range(n):
            d[words[i]] = d.get(words[i], 0) + 1

        h = []

        for key, value in d.items():
            heapq.heappush(h, (-value, key))

        for i in range(k):
            _ , key = heapq.heappop(h)
            result.append(key)

        return result
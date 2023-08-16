class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1 = len(word1)
        n2 = len(word2)
        if n1 != n2:
            return False
        d1 = collections.defaultdict(lambda: 0)
        d2 = collections.defaultdict(lambda: 0)
        for i in range(n1):
            d1[word1[i]] += 1
        for i in range(n2):
            d2[word2[i]] += 1
        list1 = sorted(d1.values())
        list2 = sorted(d2.values())
        return list1 == list2 and set(word1) == set(word2)

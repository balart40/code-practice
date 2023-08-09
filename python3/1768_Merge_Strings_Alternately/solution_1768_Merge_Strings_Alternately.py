class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pt1 = pt2 = 0
        n1 = len(word1)
        n2 = len(word2)
        result = []
        while pt1 < n1 or pt2 < n2:
            if pt1 < n1:
                result.append(word1[pt1])
            if pt2 < n2:
                result.append(word2[pt2])
            pt1 += 1
            pt2 += 1
        return ''.join(result)
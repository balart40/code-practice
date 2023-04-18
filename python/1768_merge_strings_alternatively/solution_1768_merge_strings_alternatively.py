class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n = len(word1)
        m = len(word2)
        nm = max(n,m)
        result = ""
        for i in range(nm):
            if i < n:
                result += word1[i]
            if i < m:
                result += word2[i]
        return result

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        n1 = len(word1)
        n2 = len(word2)

        if n1 != n2:
            return False

        d1 = dict()
        d2 = dict()
        s1 = set()
        s2 = set()

        for i in range(n1):
            d1[word1[i]] = d1.get(word1[i], 0) + 1
            d2[word2[i]] = d2.get(word2[i], 0) + 1
            s1.add(word1[i])
            s2.add(word2[i])

        freqs_1 = d1.values()
        freqs_2 = d2.values()
        freqs_1.sort()
        freqs_2.sort()

        if s1 == s2 and freqs_1 == freqs_2:
            return True
        else:
            return False
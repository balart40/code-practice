class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {"a" : "a", "e" : "e", "i" : "i", "o" : "o", "u" : "u", "A": "A", "E": "E", "I": "I", "O": "O", "U": "U"}
        s = list(s)

        idx_vowel = []
        for i in range(len(s)):
            if s[i] in d:
                idx_vowel.insert(0, s[i])

        for i in range(len(s)):
            if s[i] in d:
                s[i] = idx_vowel.pop(0)
        return ''.join(s)
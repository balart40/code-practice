class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = {"a": 0, "e" : 0, "i": 0, "o": 0, "u": 0}
        max_vowels = curr_vowels = 0
        for i in range(len(s)):
            if s[i] in d:
                curr_vowels += 1
            if i>= k and s[i - k] in d:
                curr_vowels -= 1
            max_vowels = max(max_vowels, curr_vowels)
        return max_vowels
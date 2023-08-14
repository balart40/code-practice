class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        d = {"a": "a", "e":"e", "i": "i", "o": "o", "u":"u"}
        counter = max_vowels = 0
        n = len(s)
        for i in range(n):
            if s[i] in d:
                counter += 1
            if i >= k and s[i - k] in d:
                counter -= 1
            max_vowels = max(max_vowels, counter)
        return max_vowels
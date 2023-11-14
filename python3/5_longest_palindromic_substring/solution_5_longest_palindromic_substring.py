import functools
class Solution:

    def longestPalindrome(self, s: str) -> str:
        start = end = max_len = 0
        result = ""
        @functools.cache
        def longestPalindrome_rec(start, end):
            nonlocal max_len, result, s
            if not s or start < 0 or end >= len(s) or s[start] != s[end]: return
            if (end - start + 1) > max_len:
                max_len = end - start + 1
                result = s[start : end + 1]
            longestPalindrome_rec(start - 1, end + 1)

        for start in range(len(s)):
            longestPalindrome_rec(start, start)
            longestPalindrome_rec(start, start + 1)
        return result
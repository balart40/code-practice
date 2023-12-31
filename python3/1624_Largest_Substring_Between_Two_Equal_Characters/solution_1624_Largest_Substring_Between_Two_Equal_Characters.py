class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        result = -1
        d = collections.defaultdict(int)
        for i in range(len(s)):
            if s[i] in d:
                result = max(result, i - d[s[i]] - 1)
            else:
                d[s[i]] = i
        return result
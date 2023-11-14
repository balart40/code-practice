class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s) < 3: return 0
        elif len(s) == 3: return 1 if s[0] == s[2] else 0
        else:
            d = collections.defaultdict(list)
            result = 0
            for i, char in enumerate(s):
                d[char].append(i)
            for key in d:
                if len(d[key]) < 2: continue
                start = d[key][0]
                end = d[key][-1]
                result += len(set(s[start + 1: end]))
            return result

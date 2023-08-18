class Solution:
    def romanToInt(self, s: str) -> int:
        d = dict()
        d["I"] = 1
        d["V"] = 5
        d["X"] = 10
        d["L"] = 50
        d["C"] = 100
        d["D"] = 500
        d["M"] = 1000
        n = len(s)
        result = 0
        for i in range(n - 1):
            if d[s[i]] < d[s[i + 1]]:
                result -= d[s[i]]
            else:
                result += d[s[i]]
        return result + d[s[-1]]
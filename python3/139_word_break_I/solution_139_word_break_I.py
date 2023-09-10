class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        max_len = max(map(len, wordDict))
        for i in range(1, n +  1):
            # originally was for j in range(i)
            # the range below optimize for words no longer than max word length
            for j in range(i - 1, max(i - max_len -1, -1), -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]
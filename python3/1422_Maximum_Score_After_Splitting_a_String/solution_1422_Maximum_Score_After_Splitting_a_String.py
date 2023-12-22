class Solution:
    def maxScore(self, s: str) -> int:
        if not s: return 0
        left = 1 if s[0] == "0" else 0
        right = sum(int(i) for i in s[1:])
        curr_max = result = left + right
        for i in range(1,len(s)-1):
            if s[i] == "0":
                left += 1
            else:
                right -= 1
            curr_max = left + right
            result = max(curr_max, result)
        return result
class Solution:
    def numberOfMatches(self, n: int) -> int:
        result = 0
        while n > 1:
            result += n // 2
            n = n // 2 if n % 2 == 0 else n // 2 + 1
        return result
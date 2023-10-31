class Solution:
    def reverse(self, x: int) -> int:
        isNegative = True if x < 0 else False
        x = int(str(x)[1:]) if isNegative else x
        MIN = -1 * 2 ** 31
        MAX = 2 ** 31 - 1
        result = "0"
        while x:
            if x < 10:
                result += str(x % 10)
                break
            rem = x % 10
            result += str(rem)
            x = x // 10
        result = -1 * int(result) if isNegative else int(result)
        if MIN <= result <= MAX:
            return result
        else: return 0
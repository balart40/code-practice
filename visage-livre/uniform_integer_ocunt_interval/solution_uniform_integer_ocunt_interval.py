
class Solution(object):
    def getUniformIntegerCountInInterval(self, A: int, B: int) -> int:
        count = 0
        for i in range(1, 10):
            x = i
            while x <= B:
                if x >= A:
                    count += 1
                x = x * 10 + i
        return count
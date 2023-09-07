from typing import List

class Solution(object):
    def getMinimumDeflatedDiscCount(self, N: int, R: List[int]) -> int:
        count = 0
        if len(R) == 1:
            return 0
        prev = R.pop()
        while R:
            if R[-1] < prev:
                prev = R[-1]
            else:
                prev -= 1
                if prev == 0:
                    return -1
                count += 1
            R.pop()
        return count
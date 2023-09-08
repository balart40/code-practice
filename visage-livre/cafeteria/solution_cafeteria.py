from typing import List
import math
class Solution(object):

    def getMaxAdditionalDinersCount(self, N: int, K: int, M: int, S: List[int]) -> int:
        S.sort()
        start, result = 1, 0
        S.append(N + K + 1)
        for taken_seat in S:
            delta = taken_seat - K - start
            if delta > 0:
                result += math.ceil(delta / (K + 1))
            start = taken_seat + K + 1
        return result
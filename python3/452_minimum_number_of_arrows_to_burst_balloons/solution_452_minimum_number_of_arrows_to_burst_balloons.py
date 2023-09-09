from typing import List
from collections import deque

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) ==  1:
            return 1
        points.sort(key=lambda x : x[0])
        def merge_intervals() -> List[List[int]]:
            nonlocal points
            result = [points[0]]
            for curr_start, curr_end in points[1:]:
                prev_end = result[-1][1]
                prev_start = result[-1][0]
                if curr_start <= prev_end:
                    result[-1][0] = max(prev_start, curr_start)
                    result[-1][1] = min(prev_end, curr_end)
                else:
                    result.append([curr_start, curr_end])
            return result

        result = merge_intervals()
        return len(result)
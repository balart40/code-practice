class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals.pop(0)[1]
        result = 0
        for left, right in intervals:
            if left < prev:
                result += 1
                if right > prev:
                    continue
            prev = right
        return result
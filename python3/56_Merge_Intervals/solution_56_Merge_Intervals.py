class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if not intervals: return intervals
        if len(intervals) == 1: return intervals

        overlap = False
        result = []

        a, b = 0, 0

        while intervals:
            if not overlap:
                a, b = intervals.pop(0)
                if not intervals:
                    result.append([a, b])
                    return result
            c, d = intervals[0]
            if c <= b <= d or c <= a <= d or a <= c <= b or a <= d <= b:
                overlap = True
                a = min(a, b, c, d)
                b = max(a, b, c, d)
                intervals.pop(0)
                if not intervals:
                    result.append([a, b])
                    return result
            else:
                result.append([a, b])
                overlap = False
        return result
"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """

        # Flatten all intervals in one list
        intervals = []
        for employe in schedule:
            for interval in employe:
                intervals.append([interval.start, interval.end])

        # sort intervals
        intervals.sort(key=lambda x : x[0])

        def mergeIntervals(intervals):
            mergedIntervals = []
            overlap = False
            a, b = 0, 0
            while intervals != []:
                if not overlap:
                    a, b = intervals.pop(0)
                    if intervals == []:
                        mergedIntervals.append([a,b])
                        break
                c, d = intervals[0]
                if c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b:
                    a = min(a, b, c, d)
                    b = max(a, b, c, d)
                    overlap = True
                    intervals.pop(0)
                    if intervals == []:
                        mergedIntervals.append([a,b])
                        break
                else:
                    mergedIntervals.append([a,b])
                    overlap = False
            return mergedIntervals

        # merge the intervals
        mergedIntervals = mergeIntervals(intervals)

        result = []
        if len(mergedIntervals) == 1:
            result.append(Interval(mergedIntervals[0][0],mergedIntervals[0][1]))
            return result
        # Get intervals where there is no work
        for i in range(1,len(mergedIntervals)):
            prevEnd = mergedIntervals[i-1][1]
            currStart = mergedIntervals[i][0]
            result.append(Interval(prevEnd,currStart))
        return result

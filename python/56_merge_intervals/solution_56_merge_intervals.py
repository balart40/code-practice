class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key= lambda x: x[0])
        result = []
        if len(intervals) == 1:
            return intervals
        '''
        while intervals != []:
            a, b = intervals.pop(0)
            i = len(intervals) - 1
            while i >= 0 and intervals is not []:
                c, d = intervals[i]
                if c <= b <= d or c <= a <= d or a <= c <= b or a <= d <= b:
                    a = min(a, b, c, d)
                    b = max(a, b, c, d)
                    intervals.pop(i)
                    i = len(intervals)
                    if intervals == []:
                        result.append([a,b])
                        return result
                i -= 1
            result.append([a, b])
        '''
        overlap = False
        a,b = 0,0
        while intervals != []:
            if not overlap:
                a, b = intervals.pop(0)
                if intervals == []:
                    result.append([a,b])
                    return result
            c, d = intervals[0]
            if c <= b <= d or c <= a <= d or a <= c <= b or a <= d <= b:
                a = min(a, b, c, d)
                b = max(a, b, c, d)
                intervals.pop(0)
                overlap = True
                if intervals == []:
                    result.append([a,b])
                    return result
            else:
                result.append([a, b])
                overlap = False
        return result

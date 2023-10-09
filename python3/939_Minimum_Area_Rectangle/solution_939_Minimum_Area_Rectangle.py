class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort()
        points_set = set([tuple(point) for point in points])
        smallest = float('inf')
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i:]):
                if x2 > x1 and y2 > y1 and (x1,y2) in points_set and (x2, y1) in points_set:
                    curr_area = (x2 - x1) * (y2 - y1)
                    smallest = min(smallest, curr_area)
        return smallest if smallest != float('inf') else 0
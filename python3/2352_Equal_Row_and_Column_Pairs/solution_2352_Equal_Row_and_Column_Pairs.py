class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        transpose = Counter(zip(*grid))
        grid = Counter(map(tuple,grid))
        return sum(transpose[i]*grid[i] for i in transpose)

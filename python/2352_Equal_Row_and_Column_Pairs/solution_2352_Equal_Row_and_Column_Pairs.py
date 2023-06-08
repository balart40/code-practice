class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        # transponse with zip(*) then Counter
        transponse_grid = Counter(zip(*grid))
        # use map since tuples are hashable
        grid = Counter(map(tuple, grid))

        for transposed_row in transponse_grid:
            result += transponse_grid[transposed_row] * grid[transposed_row]

        return result
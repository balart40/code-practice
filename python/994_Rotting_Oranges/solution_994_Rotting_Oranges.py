class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        rotten_count =  orange_count = 0
        rotten_oranges = []
        # get counts of oranges
        for i in range(m):
            orange_count += grid[i].count(1)
            rotten_count += grid[i].count(2)
            for j in range(n):
                if grid[i][j] ==  2:
                    rotten_oranges.append((i,j))
        # edge cases
        if orange_count == 0:
            return 0
        if rotten_oranges == []:
            return -1
        # initialize
        visited = grid
        minute = -1
        deltas = [(1, 0),(-1, 0),(0, -1),(0, 1)]
        # BFS on each rotten
        while rotten_oranges != []:
            rotten_oranges_length = len(rotten_oranges)
            while rotten_oranges_length > 0:
                x, y = rotten_oranges.pop(0)
                rotten_oranges_length -= 1
                for dx, dy in deltas:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and visited[i][j] == 1:
                        visited[i][j] = 2
                        orange_count -= 1
                        rotten_oranges.append((i, j))
            # 1 minute to infect neighbor oranges
            minute += 1

        return minute if orange_count == 0 else -1


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = list(grid)
        n = len(grid)
        m = len(grid[0])
        islands = 0
        for i in range(n):
            for j in range(m):
                # found an island
                if grid[i][j] == "1" and visited[i][j] == "1":
                    #print "island"
                    #print [i,j]
                    stack = []
                    islands += 1
                    # visit
                    visited[i][j] = "0"
                    stack.insert(0,[i,j])
                    #BFS or DFS
                    row = column = 0
                    while stack != []:
                        #print "stack"
                        #print stack
                        row, column = stack.pop(0)
                        visited[row][column] = 0
                        #RIGHT
                        if column + 1 < m and visited[row][column + 1] == "1" and grid[row][column + 1] == "1":
                            stack.insert(0,[row, column + 1])
                        #LEFT
                        if column - 1 >= 0 and visited[row][column - 1] == "1" and grid[row][column - 1] == "1":
                            stack.insert(0,[row, column - 1])
                        #UP
                        if row - 1 >= 0 and visited[row - 1][column] == "1" and grid[row - 1][column] == "1":
                            stack.insert(0,[row - 1,column])
                        #DOWn
                        if row + 1 < n and visited[row + 1][column] == "1" and grid[row + 1][column] == "1":
                            stack.insert(0,[row + 1, column])
        return islands
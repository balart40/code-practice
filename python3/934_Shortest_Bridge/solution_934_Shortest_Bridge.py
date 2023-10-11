class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, j = next((i,j) for i in range(m) for j in range(n) if grid[i][j])

        # dfs
        stack = [(i,j)]
        seen = set(stack)
        while stack:
            i, j = stack.pop()
            seen.add((i,j))
            for ii, jj in (i + 1, j),  (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] and (ii,jj) not in seen:
                    stack.append((ii,jj))
                    seen.add((ii,jj))

        # bfs
        ans = 0
        queue = list(seen)
        while queue:
            new_queue = []
            for i, j in queue:
                for ii, jj in (i + 1, j),  (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= ii < m and 0 <= jj < n and (ii,jj) not in seen:
                        if grid[ii][jj] == 1: return ans
                        new_queue.append((ii,jj))
                        seen.add((ii,jj))
            queue = new_queue
            ans += 1
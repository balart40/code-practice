class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = collections.defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            d[a].append([a, values[i]])
            d[b].append([b, 1 / values[i]])

        def bfs(source, target):
            nonlocal d
            if source not in d or target not in d:
                return -1
            queue, visited = collections.deque(), set()
            queue.append([source, 1])
            visited.add(source)
            while queue:
                num, wei = queue.popleft()
                if num == target:
                    return wei
                for neigh, neighweigh in d[num]:
                    if neigh not in visited:
                        queue.append([neigh, wei * neighweigh])
                        visited.add(neigh)
            return -1

        return [bfs(q[0], q[1]) for q in queries]
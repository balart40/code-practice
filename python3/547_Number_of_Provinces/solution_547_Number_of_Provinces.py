class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [1] * n

        def find_parent(city):
            while city != parent[city]:
                parent[city] = parent[parent[city]]
                city = parent[city]
            return city

        def union(city_one, city_two):
            p1, p2 = find_parent(city_one), find_parent(city_two)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1

        for i in range(n):
            for j in range(i):
                if isConnected[i][j]:
                    n-= union(i,j)
        return n
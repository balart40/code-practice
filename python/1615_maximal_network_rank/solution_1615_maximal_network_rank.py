class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # create connections as a set to avoid replication
        connecions = {i: set() for i in range(n) }
        for i, j in roads:
            connecions[i].add(j)
            connecions[j].add(i)

        max_network_rank = 0
        # iterate through all nodes except ourserlves
        for i in range(n-1):
            # start next node but not previous
            for j in range(i+1,n):
                # add connections and remove if they have duplicate
                max_network_rank = max( max_network_rank,
                                        len(connecions[i]) + len(connecions[j]) - (j in connecions[i]))

        return max_network_rank
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = 0
        n = len(cost)
        dp_zero, dp_one = cost[0], cost[1]
        for i in range(2, n):
            min_cost = cost[i] + min(dp_one, dp_zero)
            dp_zero = dp_one
            dp_one = min_cost
        return min(dp_zero, dp_one)
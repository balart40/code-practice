class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        idx_max_profit = max_profit = 0
        for i in range(1, len(prices)):
            if prices[idx_max_profit] < prices[i]:
                current_profit = prices[i] - prices[idx_max_profit]
                max_profit = max(max_profit, current_profit)
            else:
                idx_max_profit = i
        return max_profit
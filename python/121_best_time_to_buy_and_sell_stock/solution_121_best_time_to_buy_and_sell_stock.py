class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        max_profit = 0
        min_price ='inf'
        current_profit = prices[0]
        idx = 0
        for i in range(0,len(prices)):
            if prices[i]<min_price:
                min_price = prices[i]
            else:
                max_profit=max(max_profit,prices[i]-min_price)
        return max_profit
        '''
        left = 0
        right = 1
        max_profit = 0
        curr_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                curr_profit = prices[right] - prices[left]
                max_profit = max(max_profit, curr_profit)
            else:
                left = right
            right += 1
        return max_profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        max_profit = 0
        while (sell < len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
                continue
            profit = prices[sell] - prices[buy]
            if profit > max_profit:
                max_profit = profit
            sell = sell + 1
        return max_profit
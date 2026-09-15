class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        buy, sell = 0, 1

        while sell < len(prices):
            # profitable ?
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxPro = max(maxPro,profit)
            else:
                buy = sell
            sell += 1
        return maxPro




        
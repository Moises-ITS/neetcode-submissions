class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = float("-inf")
        buy = prices[0]
        for price in prices:
            if price < buy:
                buy = price
            if price - buy > sell:
                sell = price - buy
        return sell
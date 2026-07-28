class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = float("-inf")
        for price in prices:
            if price < buy:
                buy = price
            elif price - buy > sell:
                sell = price - buy
        return sell
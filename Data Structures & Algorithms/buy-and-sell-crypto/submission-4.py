class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        for p in prices:
            if p < buy:
                buy = p
            if p - buy > sell:
                sell = p - buy
        return sell
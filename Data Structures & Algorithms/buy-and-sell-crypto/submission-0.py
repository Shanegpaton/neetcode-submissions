class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        buy = prices[0]
        for i in range(len(prices)):
            total = max(total, prices[i] - buy)
            if (buy > prices[i]):
                buy = prices[i]
        return total
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        smallest, cur = prices[0], 0
        for i in range(len(prices)):
            if prices[i] < smallest:
                smallest = prices[i]
            res = max((prices[i] - smallest), res)
        return res

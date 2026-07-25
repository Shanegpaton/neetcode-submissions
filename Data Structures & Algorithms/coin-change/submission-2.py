class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            if len(dp) > coin:
                dp[coin] = 1
            for i in range(coin, len(dp)):
                    #store at amount in dp the min num of coints
                    # store the min of prev + temp
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if float('inf') ==  dp[-1] else dp[-1]
            

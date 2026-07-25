class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1
        def dfs(row, col):
            if row > m - 1 or col > n - 1:
                return 0
            if row == m - 1 or col == n - 1:
                return 1
            if dp[row][col] != -1:
                return dp[row][col]

            dp[row][col] = dfs(row + 1, col) + dfs(row, col + 1)
            return dp[row][col]
            
        return dfs(0,0)

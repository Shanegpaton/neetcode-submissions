class Solution:
    def climbStairs(self, n: int) -> int:
        total = 0
        def dfs(i):
            if i == n:
                nonlocal total
                total += 1
            if i >= n: return
            dfs(i + 1), dfs(i + 2)
        dfs(0)
        return total
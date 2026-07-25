class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, curr):
            if len(curr) == len(nums):
                res.append(curr)
                return
            
            for j in range(len(curr) + 1):
                newCurr = curr.copy()
                newCurr.insert(j, nums[i])
                dfs(i + 1, newCurr)
        dfs(0, [])
        return res

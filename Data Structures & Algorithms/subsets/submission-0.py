class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr, i):
            if i == len(nums):
                nonlocal res
                res.append(curr)
                return
            dfs(curr[:], i + 1)
            curr.append(nums[i])
            dfs(curr[:], i + 1)
        dfs([], 0)
        return res

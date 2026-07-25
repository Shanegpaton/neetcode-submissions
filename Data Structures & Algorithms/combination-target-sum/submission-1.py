class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, total, array):
            if total == target:
                res.append(array.copy())
                return
            if total > target or i >= len(nums):
                return
            array.append(nums[i])
            dfs(i, total + nums[i], array)
            array.pop()
            dfs(i + 1, total, array)
        dfs(0, 0, [])
        return res

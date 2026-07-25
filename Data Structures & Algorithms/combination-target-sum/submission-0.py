class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subarray = []
        total = 0
        def dfs(i):
            nonlocal total
            if total == target:
                res.append(subarray.copy())
                return
            if total > target or i >= len(nums):
                return 
            # look for all possible combos with i
            # call dfs with i + 1
            total += nums[i]
            subarray.append(nums[i])
            dfs(i)
            total -= nums[i]
            subarray.pop()
            dfs(i + 1)
        dfs(0)
        return res
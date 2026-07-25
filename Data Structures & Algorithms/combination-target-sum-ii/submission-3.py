class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # try add the current number and skipping the current number
        candidates.sort()
        res = set()
        def dfs(i, total, array):
            if total == target:
                res.add(tuple(array))
                return
            if total > target or i >= len(candidates):
                return
            
            array.append(candidates[i])
            dfs(i + 1, total + candidates[i], array)
            array.pop()
            dfs(i + 1, total, array)
        dfs(0, 0 , [])
        return [list(array) for array in res]
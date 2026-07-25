class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        numbers = set(nums)
        res = 1
        for num in numbers:
            if num - 1 in numbers:
                continue
            seq = 1
            while num + 1 in numbers:
                seq += 1
                num = num + 1
                res = max(res, seq)
        return res
            
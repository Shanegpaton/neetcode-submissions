class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        i = 0
        while i < (len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
            i += 1
            while nums[i] == nums[i - 1] and i < len(nums) - 2:
                i += 1
        return res
            
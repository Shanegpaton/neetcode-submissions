class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # l = 1  2  8  48
        # r = 48 48 24 6
        # multiply the left side i - 1 with the right side i + 1
        if len(nums) < 1:
            return nums
        
        l, r = [1] * len(nums), [1] * len(nums)
        l[0] = nums[0]
        for i in range(1, len(nums)):
            l[i] = l[i - 1] * nums[i]
        r[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            r[i] = nums[i] * r[i + 1]
        
        res = [0] * len(nums)
        res[0] = r[1]
        res[-1] = l[-2]
        for i in range(1, len(nums) - 1):
            res[i] = l[i - 1] * r[i + 1]
        return res
        
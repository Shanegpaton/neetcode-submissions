class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        z = 0
        for num in nums:
            if num == 0:
                z += 1
                continue
            product *= num
        res = [0] * len(nums)
        if z >= 2:
            return res
        if z == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = product
            return res
        return [int(product / num) for num in nums]
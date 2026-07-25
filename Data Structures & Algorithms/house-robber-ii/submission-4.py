class Solution:
    def rob(self, nums: List[int]) -> int:
        # check the max on all but the last and all but the first
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0 ]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        left1, left2 = 0, 0
        for i in range(len(nums) - 1):
            temp = max(left2 + nums[i], left1)
            left2 = left1
            left1 = temp
        firstMax = left1
        left1, left2 = 0, 0
        for i in range(1, len(nums)):
            temp = max(left2 + nums[i], left1)
            left2 = left1
            left1 = temp
        return max(left1, firstMax)
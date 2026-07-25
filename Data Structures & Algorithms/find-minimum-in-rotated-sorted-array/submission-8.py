class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 
        if nums[l] < nums[r]:
            return nums[l]
        while l < r:
            middle = (r + l) // 2
            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle 
        return nums[l]
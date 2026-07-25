class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left pointer at start right pointer at start
        # if nums at half it length is less than targer move l to there
        # else move r to there
        # keep loopping while l < r or checking val is target return true
        l, r = 0, len(nums) - 1
        while (l <= r):
            check = ((r - l) // 2) + l
            if (nums[check] == target):
                return check
            if nums[check] < target:
                l = check + 1
            else: 
                r = check - 1
        return -1
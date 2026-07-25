class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            middle = (r + l) // 2
            if nums[middle] == target:
                return middle
             # if you in the left sorted arrar check the left pointer to see if it is between
            if nums[middle] >= nums[l]:
                if nums[l] <= target and nums[middle] >= target:
                    r = middle
                else: 
                    l = middle + 1
            # if you are in the right array check teh right pointer to see if it is betwee
            else:
                if nums[r] >= target and nums[middle] < target:
                    l = middle
                else:
                    r = middle - 1
        return -1

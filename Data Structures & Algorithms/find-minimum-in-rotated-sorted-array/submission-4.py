class Solution:
    def findMin(self, nums: List[int]) -> int:
        # move left pointer when the middle value is greater 
        # move the right pointer when the middle value is less than it
        l, r = 0, len(nums) - 1 
        while l < r:
            middle = (r + l) // 2
            if nums[middle] >= nums[l] or nums[middle] >= nums[r]:
                if (nums[l] < nums[r]):
                    r = middle - 1
                else: 
                    l = middle + 1
            else:
                # look for bigger pointer
                if nums[l] > nums[r]:
                    r = middle
                else:
                    l = middle
        return nums[l]

# if the middle is higher we need to look between the lower values
# if the middle is lower we need to look between the higher values

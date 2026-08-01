class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find piviot and return index if none return len
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            # check mid if it is higher that left look right
            # else look left?
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]

# check if len - 1 needed on line 6
    # [ 3, 4, 5, 6, 1, 2] 
    # [ 5, 6, 1, 2, 3 ,4] 

    
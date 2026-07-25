class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #left bound binary search
        lower, upper = 0, len(nums)
        while lower < upper:
            mid = (upper + lower) // 2
            if nums[mid] == target:
                return mid
            elif  target < nums[mid]:
                upper = mid
            else:
                lower = mid + 1
        return -1


# we need to find the left most target value
# while the right pointer is greaterthan or = to keep moving it to the middle
# move the left pointer to the middle + 1
# return left pointer
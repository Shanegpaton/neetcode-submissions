class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # exact binary search
        lower, upper = 0, len(nums) - 1
        while lower <= upper:
            mid = (upper + lower) // 2
            if nums[mid] == target:
                return mid
            elif  target < nums[mid]:
                upper = mid - 1
            else:
                lower = mid + 1
        return -1


# we need to find the left most target value
# while the right pointer is greaterthan or = to keep moving it to the middle
# move the left pointer to the middle + 1
# return left pointer
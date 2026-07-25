class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # upperBounded binary search
        l, r = 0, len(nums) 
        while l < r:
            mid = l + (r - l) // 2 
            if target >= nums[mid]:
                l = mid + 1
            else:
                r = mid 
        return l - 1 if nums[l - 1] == target else -1


# find the right most target value
# while the mid is less than or = move it to left to mid


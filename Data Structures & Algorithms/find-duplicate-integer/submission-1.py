class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # start at 0 and follow its path with a fast and slow pointer until the intersect
        slow, fast = 0, 0
        while True:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
            if nums[fast] == nums[slow]:
                break
        # after intersections add a slow pointer at 0 and move both slow pointers until intersection
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow
        
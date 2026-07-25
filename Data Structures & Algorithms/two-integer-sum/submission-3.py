class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # check if set has target - num
        scan = {} # num index
        for i in range(len(nums)):
            num = nums[i]
            if target - num in scan:
                return [scan[target - num], i]
            scan[num] = i 
        
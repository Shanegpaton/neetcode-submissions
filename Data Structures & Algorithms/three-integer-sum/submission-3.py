class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return all unique triplets where their sum = 0 in any order
        # iterate through the list with index i
        # if i is the same as last time remove it
        # place a pointer l directly after i and pointer r at the end
        # if the sum of nums at i l and r == 0 add it to the solution array
        # loop withing the i loop until l <= r
        trips = []
        nums.sort()
        for i in range(len(nums) - 2):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            l, r = i + 1, len(nums) - 1
            while (l < r):
                if (l > i + 1 and nums[l] == nums[l - 1]):
                    l += 1
                    continue
                if (r < len(nums) - 1 and nums[r] == nums[r + 1]):
                    r -= 1
                    continue
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    trips.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return trips

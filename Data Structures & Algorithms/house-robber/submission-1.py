class Solution:
    def rob(self, nums: List[int]) -> int:
        # you can pick to skip last and then do the max of the 2 left
        # or skip and to 2 left plus 1 left
        twoLeft = 0
        left = 0
        for num in nums:
            temp = max(left, twoLeft + num)
            twoLeft = left
            left = temp
        return left
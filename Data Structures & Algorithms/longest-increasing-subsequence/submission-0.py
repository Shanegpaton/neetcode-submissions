class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # create dp[] holding the best value from that point on 
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        
        return max(dp)
            

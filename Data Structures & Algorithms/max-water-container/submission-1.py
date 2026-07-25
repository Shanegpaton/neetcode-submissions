class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # put pointers at each end an move in the shorter pointer
        # update max
        maxH = 0
        l, r = 0, len(heights) - 1
        while l < r:
            # calc max
            maxH = max(maxH, min(heights[l], heights[r]) * (r - l))
            # move shorter pointer inwards
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return maxH
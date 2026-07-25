class Solution:
    def trap(self, height: List[int]) -> int:
        # each height if filled with the min(l, r) - height
        total = 0
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r] 
        while (l < r):
            if (lMax < rMax):
                l += 1
                if (height[l] > lMax):
                    lMax = height[l]
                total += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                total += rMax - height[r]

        return total
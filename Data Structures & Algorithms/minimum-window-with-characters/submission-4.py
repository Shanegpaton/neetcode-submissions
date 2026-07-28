class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # slide a window. move right. when the right most is a dup letter 
        # slide the left side in until there is a none dup. 
        # keep the result as the l,r
        resL, resR = 0, len(s)
        l, r = 0, 0
        validCounter = 0
        windowCount = defaultdict(int)
        targetCount = defaultdict(int)
        for letter in t:
            targetCount[letter] += 1
        while r < len(s):
            if windowCount[s[r]] < targetCount[s[r]]:
                validCounter += 1
            windowCount[s[r]] += 1
            while windowCount[s[l]] > targetCount[s[l]] and l < r:
                l += 1
                windowCount[s[l - 1]] -= 1
            if resR - resL > r - l and validCounter == len(t):
                resR = r
                resL = l
            r += 1
        return s[resL: resR + 1] if validCounter == len(t)  else ""

            
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        letters = defaultdict(int)
        while r < len(s):
            while letters[s[r]] > 0:
                letters[s[l]] -= 1
                l += 1
            letters[s[r]] += 1
            r += 1
            res = max(res, r - l)
        return res

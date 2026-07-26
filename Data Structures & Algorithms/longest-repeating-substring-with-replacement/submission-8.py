class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l, r = 0, 0
        letters = defaultdict(int)
        maxFreq = 0 
        while r < len(s):
            letters[s[r]] += 1
            maxFreq = max(letters[s[r]], maxFreq)
            while r - l + 1 > maxFreq + k:
                l += 1
                letters[s[l - 1]] -= 1
            res = max(res, r - l + 1)
            r += 1
        return res


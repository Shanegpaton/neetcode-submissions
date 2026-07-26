class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l, r = 0, 0
        letters = defaultdict(int)
        while r < len(s):
            letters[s[r]] += 1
            most = self.getMostFreq(letters, s, r)
            maxFreq = letters[most]
            while r - l + 1 > maxFreq + k:
                l += 1
                letters[s[l - 1]] -= 1
            res = max(res, r - l + 1)
            r += 1
        return res


    def getMostFreq(self, letters, s: str, r: int):
        mostFreq, highCount = letters[r], 0
        for letter in letters:
            if highCount < letters[letter]:
                highCount = letters[letter]
                mostFreq = letter
        return mostFreq
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       # hold the each char freq in the window in an array
       # if the grreated freq + window len > k move left pointer
        l = 0
        longest = 0
        freq = [0] * 26
        maxFreq = 0
        for r in range(len(s)):
            freq[ord(s[r]) - ord('A')] += 1
            maxFreq = max(maxFreq, freq[ord(s[r]) - ord('A')])
            while not (maxFreq + k >= r - l + 1):
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest

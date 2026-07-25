class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # look for the longest substring without duplicates in s
        # loop through s char by char, storing each char in a hashset updating max len
        # when a duplicate is found, remove the first occurance of the letter max --
        if len(s) == 0:
            return 0
        characters = set()
        l = 0
        characters.add(s[0])
        total = 1
        for r in range(1, len(s)):
            while (s[r] in characters):
                characters.remove(s[l])
                l += 1
            characters.add(s[r])
            total = max(total, len(characters))
        return total
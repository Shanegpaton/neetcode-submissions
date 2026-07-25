class Solution:
    def longestPalindrome(self, s: str) -> str:
       # for every letter assume it as the middle
       # put a pointer left and right of it and move them out as they match saving the largest value
       # test each side if it holds the same value then move only it
        if not s:
            return ""
        
        longest = s[0]
        def check(l, r):
            while l > 0 and r < len(s) - 1:
                if s[l  - 1] == s[r + 1]:
                    l -= 1
                    r += 1
                else:
                    return l, r
            return l, r
        for i, char in enumerate(s):
            l, r = check(i, i)
            if r - l > len(longest) - 1:
                longest = s[l:r + 1]
            # try moving left one
            if i > 0:
                if s[i] == s[i - 1]:
                    l, r = check(i - 1, i)
                    if r - l > len(longest) - 1:
                        longest = s[l:r + 1]
            
        return longest

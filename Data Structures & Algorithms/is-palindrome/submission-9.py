class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        if s == "":
            return False
        l, r = 0, len(s) - 1
        while l < r:
            while l < len(s) - 1 and not self.isValid(s[l]):
                l += 1
            while r > 0 and not self.isValid(s[r]):
                r -= 1
            if s[l] != s[r] and l < r:
                return False
            l += 1
            r -= 1
        return True

    def isValid(self, c: str) -> bool:
        if ord(c) >= ord("a") and ord(c) <= ord("z"):
            return True
        if ord(c) >= ord('0') and ord(c) <= ord("9"):
            return True
        return False

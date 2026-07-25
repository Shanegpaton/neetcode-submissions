class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # move the right pointer forward and check if the char is closer to substring
        # check if r - l is the length of s1
        # move l until it decrements the extra letter
        l = 0
        characters = [0] * 26
        for i in range(len(s1)):
            index = ord(s1[i]) - ord('a')
            characters[index] += 1
        for r in range(len(s2)):
            rIndex = ord(s2[r]) - ord('a')
            characters[rIndex] -= 1
            if (characters[rIndex] == -1):
                while not (s2[l] == s2[r]):
                    lIndex = ord(s2[l]) - ord('a')
                    characters[lIndex] += 1
                    l += 1
                lIndex = ord(s2[l]) - ord('a')
                characters[lIndex] += 1
                l += 1
            if (r - l + 1 == len(s1)):
                return True
        return False

            # if r is in s2 decromnet the letter in letters
                # if r - l + 1 = s1 return true
            # else slide left until the -1 become 0
        
# the window length will only grow when we find a value needed
# when r - l + 1 == s1 len return true
# 
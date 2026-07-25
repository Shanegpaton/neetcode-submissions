class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(t) == 1 and t[0] == s[0]):
            return s[0]
        shortestString = ""
        shortestL = shortestR = 0
        l = 0
        characters = {}
        count = 0
        for i in range(len(t)):
            characters[t[i]] = characters.get(t[i], 0) + 1
        for r in range(len(s)):
            # increment right
            if (s[r] in characters):
                characters[s[r]] -= 1
                if (characters[s[r]] >= 0):
                    count += 1
                
            # incrmenet left while it points to a char with less than 0 occurances in the map is not found
            while (r >= l and (s[l] not in characters or characters[s[l]] < 0) ):
                if (s[l] not in characters):
                    l += 1
                else:  
                    characters[s[l]] += 1
                    l += 1
            if (count == len(t)):
                    if (shortestR > 0):
                        currentSize = shortestR - shortestL + 1
                        windowSize = r - l + 1
                        if (windowSize < currentSize):
                            shortestL = l
                            shortestR = r
                    else :
                        shortestL = l
                        shortestR = r
        if (shortestR == 0):
            return ""
        return s[shortestL : shortestR + 1]
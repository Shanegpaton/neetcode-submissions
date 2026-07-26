class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        for i in range(len(s)):
            letters = defaultdict(int)
            for letter in t:
                    letters[letter] += 1
            for j in range(i, len(s)):
                if letters[s[j]] > 0:
                    letters[s[j]] -= 1
                valid = True
                for letter in letters:
                    if letters[letter] > 0:
                        valid = False
                if valid:
                    if j - i + 1 < len(res) or len(res) == 0:
                        res = s[i:j + 1]
        return res
            
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                # if the index - len of word is in bound
                # and the word == s from current - len(word) to current
                # and dp at curr - len(word) == true
                if i - len(word) >= 0 and dp[i - len(word)] and s[i - len(word): i] == word:
                    dp[i] = True
                if dp[i]:
                    break
                
        return dp[-1]
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        indexes = set()
        def dfs(l, r):
            if r >= len(s):
                return
            nonlocal indexes
            if r in indexes:
                return
            if s[l: r + 1] in wordDict:
                indexes.add(r)
                dfs(r + 1, r + 1)
            dfs(l, r + 1)
        dfs(0,0)
        return True if len(s) - 1 in indexes else False
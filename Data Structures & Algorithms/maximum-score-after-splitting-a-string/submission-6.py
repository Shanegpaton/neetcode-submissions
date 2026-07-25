class Solution:
    def maxScore(self, s: str) -> int:
        zeros, ones = 0, 0
        lscore, rscore= [0] * len(s), [0] * len(s)
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            lscore[i] = zeros
        for i in range(len(s) - 1, 0, -1):
            if s[i] == '1':
                ones += 1
            rscore[i] = ones
        r = lscore[0] + rscore[1]
        print(rscore)
        print(lscore)
        for i in range(len(s) - 1):
            r = max(r, lscore[i] + rscore[i + 1])
        return r

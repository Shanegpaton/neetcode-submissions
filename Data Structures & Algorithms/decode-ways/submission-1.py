class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        # dp variables: a = dp[i-2], b = dp[i-1]
        a, b = 1, 1
        
        for i in range(1, len(s)):
            temp = 0
            # Single digit decode (s[i] != '0')
            if s[i] != '0':
                temp += b
            # Two digit decode (10 <= s[i-1:i+1] <= 26)
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                temp += a
            a, b = b, temp  # move window forward
            if b == 0:  # no valid decoding
                return 0
        
        return b

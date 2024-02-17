class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) +1 )
        dp[0]=1
        if s[0] == "0":
            return 0
        for i in range( len(s) ):
            if s[i] != "0":
                dp[i+1] += dp[i]
            if i > 0 and 10 <= int(s[i-1:i+1]) <= 26:
                dp[i+1] += dp[i-1]
        return dp[-1]

s = Solution()
print(s.numDecodings("10"))
print(s.numDecodings("1123"))
print(s.numDecodings("06"))
print(s.numDecodings("12"))
print(s.numDecodings("226"))
print(s.numDecodings("11106"))
1,1,2,3
11,2,3
1,12,3
1,1,23
11,23
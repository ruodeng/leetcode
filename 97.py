class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1length,s2length,s3length=len(s1),len(s2),len(s3)
        if s1length+s2length!=s3length:
            return False
        # dp[i][j] means s1[:i] and s2[:j] can form s3[:i+j]
        dp=[[False]*(s2length+1) for _ in range(s1length+1)]
        dp[0][0]=True
        for i in range(1,s1length+1):
            dp[i][0]=dp[i-1][0] and s1[i-1]==s3[i-1]

        for j in range(1,s2length+1):
            dp[0][j]=dp[0][j-1] and s2[j-1]==s3[j-1]
        for i in range(1,s1length+1):
            for j in range(1,s2length+1):
                dp[i][j]=(dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        # print('=========================')
        # for i in range(1,s2length+1):
        #     print(dp[i])
        return dp[-1][-1]

s = Solution()
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # True
# print(s.isInterleave("", "", ""))  # True
# print(s.isInterleave("a", "", ""))  # True

# i,j=1,1

# # "a","b","ab"
# True, False
# True,
# # "aa","b","aab"
# True, False, False
# True, False,
# True, True,
# 1,1= 0,1 and s1[0]=s3[1] or 1,0 and s2[0]=s3[1]
# ab, ab,
# 0,1 and s1[0]=s3[1],  a is in s2,   find b in s1.
# 1,0 and s2[0]=s3[1],  a is in s1, need find   b in s2.

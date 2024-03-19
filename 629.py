class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0]*(k+1)
        dp[0] =1
        for i in range(2,n+1):
            temp = [0]*(k+1)
            temp[0] = 1
            for j in range(1,k+1):
                temp[j] = (temp[j-1]+dp[j])%mod
                if j>=i:
                    temp[j] = (temp[j]-dp[j-i]+mod)%mod
            dp = temp

        return dp[k]
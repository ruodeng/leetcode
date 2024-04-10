from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        m = len(cuts)
        dp = [[0]*m for _ in range(m)]
        print(cuts)
        print(m)
        print(dp)
        for i in range(m-2,-1,-1):
            for j in range(i+2,m):
                dp[i][j] = float('inf')
                for k in range(i+1,j):
                    dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j]+cuts[j]-cuts[i])
        print(dp)
        return dp[0][m-1]
s = Solution()
print(s.minCost(7,[1,3,4,5]))

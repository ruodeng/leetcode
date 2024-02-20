from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = 2
        dp = [[0] * len(prices) for _ in range(k)]
        for kk in range(k):
            min_price = prices[0]
            for i in range(1, len(prices)):
                min_price = min(min_price, prices[i] - dp[kk - 1][i - 1])
                dp[kk][i] = max(dp[kk][i - 1], prices[i] - min_price)
        return dp[-1][-1]


s = Solution()
print(s.maxProfit([1, 4, 2]))  # 6
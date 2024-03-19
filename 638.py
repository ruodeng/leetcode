from typing import List


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        # memo={}
        # def dfs(needs):
        #     if sum(needs) == 0:
        #         return 0
        #     if tuple(needs) in memo:
        #         return memo[tuple(needs)]
        #     # not use special offer, which is the highest price
        #     res =sum([needs[i]*price[i] for i in range(len(needs))])
        #     # compare special offer
        #     for s in special:
        #         if all(needs[i] >= s[i] for i in range(len(needs))):
        #             res = min(res, dfs([needs[i]-s[i]  for i in range(len(needs))])+s[-1])
        #     memo[tuple(needs)] = res
        #     return res
        # return dfs(needs)





        max_needs = max(needs)
        # dp =[[0]* (max_needs+1) for i in range(len(needs)+1)]
        dp = [[0] * (max_needs + 1)] * (len(needs) + 1)

        for d in dp:
            print(d)

s = Solution()
price = [2,5]
special = [[3,0,5],[1,2,10]]
needs = [3,2]
print(s.shoppingOffers(price,special,needs))



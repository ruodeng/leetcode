class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        def checkNum(n,l,r):
            return n >= l and n <= r
        dp = [0] * (r-l+1)
        for i in range(len(nums)):
            if checkNum(nums[i], l, r):
                dp[i] = 1
            # nums[:i] = [n for n in nums[:i] if checkNum(n, l, r)
            nums[:i]

        for i in range(l-1, r):
            if i == 0:
            dp[i] = 1
            # for j in range(i):
            #     if nums[i] % nums[j] == 0:
            #         dp[i] += dp[j]
        # dp[i-1] +dp[i]
# 1,2,2,3
# 1,*+P,*+P
# 1
# 1,2,12
# 1,2,12,3,13,23
1,2,2,4,7   [1,5]
1,2,2
2,2
4


1 2 2,   4
1 3 3+3  6+2


[1,2,3], [6,6]
[1,2], [3,3]


[1,2,2,4],[1,5]
[1,2,2],[-3,1]
[1,2],[-5,-1]


1,2,2,4,7


1,2
     2,4

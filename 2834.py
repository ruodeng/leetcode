import math
from itertools import chain


class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:


        a = min(target // 2, n)
        b = max(0, n - a)

        return (a * (a + 1) + b * (2 * target + b - 1)) // 2

        # k = target //2
        # if n <=k:
        #     return (n+1)*n //2
        # else:
        #     return k*(k+1)//2 + (target+target+n-k-1)*(n-k)//2
        #
        #
        #
        # t = target // 2 + 1
        # t = math.isqrt(target) + 1
        # if t + t -1 >=target:
        #     t = t-1
        #     # return  (n+1)*n //2
        # total = (t+1)*t//2
        # n -= t
        # total += n*(n+1)//2 + n*(target-1)
        # return total
        # return sum (list(chain (range(1,target//2+1),
        #                         range(target,n+target//2+1)))[:n])
s = Solution()

# 24517*24516//2 =
# ss = s.minimumPossibleSum(3, 5)
# print(ss)
# ss = s.minimumPossibleSum(3, 4)
# print(ss)
# ss = s.minimumPossibleSum(3, 3)
# print(ss)
# ss = s.minimumPossibleSum(2, 3)
# print(ss)
# ss = s.minimumPossibleSum(1, 1)
# print(ss)
# ss = s.minimumPossibleSum(16, 6)
# print(ss)
# ss = s.minimumPossibleSum(13, 50)
# print(ss)
ss = s.minimumPossibleSum(39636, 49035)
print(ss)

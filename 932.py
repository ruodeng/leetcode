from typing import List


class Solution:
    memo = {}
    def beautifulArray(self, n: int) -> List[int]:
        if n in self.memo:
            return self.memo[n]
        if n == 1:
            return [1]
        else:
            self.memo[n]=[i*2-1 for i in self.beautifulArray((n+1)//2)] + [i*2 for i in self.beautifulArray(n//2)]
            return self.memo[n]
s = Solution()
print(s.beautifulArray(5))

# n: 5 3 ::: 2
# n: 3 2 ::: 1
# n: 2 1 ::: 1
# [1, 5, 3, 2, 4]
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count('1') for i in range(n+1)]
s = Solution()
print(s.countBits(5))
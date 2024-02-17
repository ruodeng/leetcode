from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        can=True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i < len(flowerbed)-1 and flowerbed[i+1] == 1:
                    can=False
                if can:
                    n -= 1
                    if n <= 0:
                        return True
                    can=False
                else:
                    can=True
            else:
                can=False
        return n <= 0
s = Solution()
ss = s.canPlaceFlowers([1,0,0,0,1], 1)
print(ss)
ss = s.canPlaceFlowers([1,0,0,0,1], 2)
print(ss)
ss = s.canPlaceFlowers([1,0,0,0,0,0,1], 2)
print(ss)
ss = s.canPlaceFlowers([1,0,0,0,0,1], 2)
print(ss)
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        res = 0
        k = len(satisfaction)-1
        total = 0
        while k >= 0 :
            res += satisfaction[k]
            if res < 0:
                break
            total += res
            k -= 1
        return total

        # -9 25
        # -8 20
        # -1 15
        # 0 10
        # 2,3,4
        # 2,12
        #
        # -1,-15
        # i,j
        # satisfaction[j] > 0
        # satisfaction[i] < 0

        -1,-8,0,5,-9
        -9,-8,-1,0,5
        5,5,4,-4,-13
        5,10,14,10



        return res

s = Solution()
print(s.maxSatisfaction([-1,-8,0,5,-9]))
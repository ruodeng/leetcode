from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        n = len(happiness)
        i=0
        total = 0
        while i < n and i < k:
            if happiness[i]-i >0:
                total+=happiness[i]-i
            else:
                break
            i+=1
        return total
s =Solution()
print(s.maximumHappinessSum([1,2,3],2))
print(s.maximumHappinessSum([1,1,1,1],2))
print(s.maximumHappinessSum([2,3,4,5],1))
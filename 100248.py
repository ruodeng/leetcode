from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s=sum(apple)
        capacity.sort(reverse=True)
        i,count =0,0
        while s >0:
            s-=capacity[i]
            i+=1
            count+=1
        if i > len(capacity):
            return -1
        return count
s = Solution()
print(s.minimumBoxes([1,3,2],[4,3,1,5,2]))
print(s.minimumBoxes([5,5,5],[2,4,2,7]))
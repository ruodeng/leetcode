from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for q in queries:
            qq = q[2]**2
            count = 0
            for p in points:
                if (p[0]-q[0])**2 + (p[1]-q[1])**2 <= qq:
                    count += 1
            ans.append(count)
        return ans
s = Solution()
print(s.countPoints([[1,3],[3,3],[5,3],[2,2]],[[2,3,1],[4,3,1],[1,1,2]]))

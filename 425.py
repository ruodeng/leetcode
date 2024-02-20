from typing import List


class Solution:

    def findMinArrowShots(self, points):
        points.sort(key=lambda x: x[1])

        total, end_point = 0, float("-inf")

        for i in points:
            if i[0] > end_point:
                total += 1
                end_point = i[1]

        return total

    # def findMinArrowShots(self, points: List[List[int]]) -> int:
    #     points.sort()
    #     count=0
    #     res = None
    #     for i in points:
    #         if not res:
    #             res = i
    #         elif  res[1] >= i[0]:
    #             res[0] = max(res[0], i[0])
    #             res[1] = min(res[1], i[1])
    #         else:
    #             count+=1
    #             res = i
    #     return count+1

s = Solution()
print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))  # 2
print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))  # 4
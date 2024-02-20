from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        if not triangle:
            return 0

        # solution one:
        # 2
        # 3,4
        # 6,5,7
        # 4,1,8,3
        # become
        # 2
        # 5, 6
        # 11, 10, 13
        # 15, 10, 18, 16
        # if len(triangle) == 1:
        #     return triangle[0][0]
        # for i in range(1, len(triangle)):
        #     for j in range(len(triangle[i])):
        #         if j == 0:
        #             triangle[i][j] += triangle[i - 1][j]
        #         elif j == len(triangle[i]) - 1:
        #             triangle[i][j] += triangle[i - 1][j - 1]
        #         else:
        #             triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        # return min(triangle[-1])

        # solution two:
        # use less space
        length = len(triangle)
        dp = [0] * length
        for i in range(length):
            for j in range(i, -1, -1):
                if j == 0:
                    dp[j] += triangle[i][j]
                elif j == i:
                    dp[j] = triangle[i][j] + dp[j-1]
                else:
                    dp[j] = triangle[i][j] + min(dp[j], dp[j-1])
            # [2, 0, 0, 0]
            # [5, 6, 0, 0]
            # [11, 10, 13, 0]
            # [15, 11, 18, 16]
        return min(dp)

s = Solution()
print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # 11


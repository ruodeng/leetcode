from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dp = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]

        dp[0][0] = grid[0][0]
        # dp[0][1] = max(grid[0][0], grid[0][1])
        # dp[1][0] = max(grid[0][0], grid[1][0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0:
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][j], grid[i][j]))
                if j > 0:
                    dp[i][j] = min(dp[i][j], max(dp[i][j - 1], grid[i][j]))




        # def dfs(i,j):
        #     # if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or dp[i][j]  == float('inf'):
        #     #     return
        #     # or dp[i][j] <= max(grid[i][j], float('-inf'))
        #     print("DFS",i,j)
        #     borders=[]
        #     for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        #         if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        #             if dp[x][y]  ==  float('inf'):
        #                 print("x,y",x,y,dp[x][y]  ==  float('inf'))
        #                 pass
        #                 # dfs(x, y)
        #             else:
        #                 borders.append((x,y))
        #     print("borders",borders)
        #     dp[i][j] = max( min([dp[x][y] for (x,y) in borders]), grid[i][j])
        # dfs(len(grid)-1,len(grid)-1)






        for d in dp:
            print(d)




s = Solution()
# print(s.swimInWater([[0, 2], [1, 3]]))
print( s.swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]))

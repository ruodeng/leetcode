from typing import List


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        dicts={}
        dicts_y={}
        n = len(grid)
        for i in range(n):
            for j in range(n):
                # in Y
                if (i==j or i+j == n-1) and i <= n//2 or i > n // 2 and j == n // 2   :
                    dicts_y[grid[i][j]] = dicts_y.get(grid[i][j],0)+1
                else:
                    dicts[grid[i][j]] = dicts.get(grid[i][j],0)+1
        sum1= sum(dicts.values())
        sum2= sum(dicts_y.values())
        max_count=float('inf')
        for i in range(3):
            count = sum1 - dicts.get(i,0)
            for j in range(3):
                if i == j:
                    continue
                max_count=min(max_count, count+ sum2-dicts_y.get(j,0))
        return max_count




s = Solution()
grid = [[1,2,2],[1,1,0],[0,1,0]]
s.minimumOperationsToWriteY(grid)
print("=====")
grid = [[0, 1, 0, 1, 0], [2, 1, 0, 1, 2], [2, 2, 2, 0, 1], [2, 2, 2, 2, 2], [2, 1, 2, 2, 2]]
s.minimumOperationsToWriteY(grid)
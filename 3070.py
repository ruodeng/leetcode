from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        count=0
        for i in range(m):
            for j in range(1,n):
                grid[i][j] += grid[i][j-1]

        for i in range(1,m):
            for j in range(n):
                grid[i][j] += grid[i-1][j]
        for i in range( m):
            for j in range(n):
                if grid[i][j] <= k:
                    count += 1

        return count

s = Solution()
grid = [[7,6,3],[6,6,1]]
k = 18
print(s.countSubmatrices(grid,k))
grid = [[7,2,9],[1,5,0],[2,6,6]]
k = 20
print(s.countSubmatrices(grid,k))
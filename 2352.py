from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count =0
        grid2 =[]
        for i in range(len(grid)):
            col =[]
            for j in range(len(grid)):
                col.append(grid[j][i])
            grid2.append(col)
        for g1 in grid:
            for g2 in grid2:
                if g1 == g2:
                    count+=1  
        return  count

        # freq = Counter(tuple(row) for row in grid)
        # return sum(freq[tuple(col)] for col in zip(*grid))

s = Solution()
# grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# print(s.equalPairs(grid))
grid=[[13,13],[13,13]]
print(s.equalPairs(grid))
grid=[[3,2,1],[1,7,6],[2,7,7]]
print(s.equalPairs(grid))
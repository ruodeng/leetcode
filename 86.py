from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        matrix2 = [[int(matrix[j][i]) for i in range(len(matrix[j]))] for j in range(len(matrix))]
        print(matrix2)
        i,j,w,h=0,0,len(matrix2),len(matrix2[0])
        total = 0
        for i in range(w):
            for j in range(h):
                total += matrix2[i][j]
                # if matrix2[i][j] == 1:
                #     total = max(total, w*h)
        print(total)
        if total < 20:

    dp[i][j]






s = Solution()
ss = s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
print(ss)
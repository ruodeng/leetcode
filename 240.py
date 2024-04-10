from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        lenm,lenn = len(matrix),len(matrix[0])
        def dfs(i,j,m,n):
            if m < 0 or n < 0 or i > m or j >n:
                return False
            if i==m:
                if j == n:
                    return matrix[i][j] == target
                else:
                    return target in matrix[i][j:n+1]
            if j == n:
                return target in [matrix[k][j] for k in range(i,m+1)]
            if m-i ==1 and n-j ==1:
                return matrix[i][j] == target or matrix[m][n] == target or matrix[m][j] == target or matrix[i][n] == target
            if matrix[i][j]>target or matrix[m][n]<target:
                return False
            k,p = (i+m)//2,(j+n)//2
            if matrix[k][p] == target:
                return True
            elif matrix[k][p] > target:
                if matrix[i][j] <= target:
                    return dfs(i,j,k,p)  or dfs(i,j,m,p-1) or dfs(i,p,k-1,n)
                return False
            else:
                if matrix[m][n] >= target:
                    print(i, j, m, n)
                    return dfs(k+1,p,m,n) or dfs(i,p+1,k,n) or dfs(k,p,m,n)
                return False
        return dfs(0,0,lenm-1,lenn-1)

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

target = 5
s = Solution()
# print(s.searchMatrix(matrix,target))
#
# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 20
# print(s.searchMatrix(matrix,target))

print(s.searchMatrix([[-5]],-5))
# print(s.searchMatrix([[1,1]],2))
# print(s.searchMatrix([[-1],[-1]],0))

# matrix=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
# target=1
# # print(s.searchMatrix(matrix,target))
# matrix=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
# target=15
# print(s.searchMatrix(matrix,target))
# matrix=[[48,65,70,113,133,163,170,216,298,389],[89,169,215,222,250,348,379,426,469,554],[178,202,253,294,367,392,428,434,499,651],[257,276,284,332,380,470,516,561,657,698],[275,331,391,432,500,595,602,673,758,783],[357,365,412,450,556,642,690,752,801,887],[359,451,534,609,654,662,693,766,803,964],[390,484,614,669,684,711,767,804,857,1055],[400,515,683,732,812,834,880,930,1012,1130],[480,538,695,751,864,939,966,1027,1089,1224]]
# target=600
# print(s.searchMatrix(matrix,target))
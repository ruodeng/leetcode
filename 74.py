from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, m
        while i < j:
            mid = (i + j) // 2
            print(i,j,mid)
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                k,l =0,n
                while k<l:
                    nid = (k+l)//2
                    if matrix[mid][nid] == target:
                        return True
                    elif matrix[mid][nid] < target:
                        k = nid+1
                    else:
                        l = nid
                return False
            elif matrix[mid][n - 1] < target:
                i = mid + 1
            elif matrix[mid][0] > target:
                j = mid

        return False


# matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# target = 3
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 11
s = Solution()
ss = s.searchMatrix(matrix, target)
print(ss)

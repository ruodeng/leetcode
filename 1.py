from typing import List


# class Solution:
#     def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         m = len(matrix)
#         n = len(matrix[0])
#         for i in range(n):
#             maxinum=-1
#             js =[]
#             for j in range(m):
#                 if matrix[j][i] == -1:
#                     js.append(j)
#                 if matrix[j][i] > maxinum:
#                     maxinum = matrix[j][i]
#             for j in js:
#                 matrix[j][i] = maxinum
#         return matrix
#
# matrix = [[3,-1],[5,2]]
# s = Solution()
# ss = s.modifiedMatrix(matrix)
# print("RE:",ss)


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        ns =[]
        count=0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                ns.append(1)
            elif nums[i] > nums[i+1]:
                ns.append(-1)
            else:
                ns.append(0)
        for i in range(len(ns)-len(pattern)+1):
            if ns[i:i+len(pattern)] == pattern:
                count += 1
        return count


s = Solution()
ss = s.countMatchingSubarrays([1,4,4,1,3,5,5,3], [1,0,-1])
print(ss)
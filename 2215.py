from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]

s = Solution()
# print(s.findDifference([1,2,3,4,5],[2,3,4,5,6]))  # [[1], [6]]
# print(s.findDifference([1,2,3],[2,4,6]))
# print(s.findDifference([1,2,3,3],[1,1,2,2]))  # [[1], [6]]
print(s.findDifference([26,48,-78,-25,42,-8,94,-68,26],[61,-17]))  # [[1], [6]]
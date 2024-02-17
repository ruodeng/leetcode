from typing import List
from collections import Counter
from heapq import heapify, heappush, heappop


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        leng = len(nums)
        i, j, count = 0, leng // 2, leng
        while i < leng // 2 and j < leng:
            if nums[i] < nums[j]:
                i += 1
                count -= 2
            j += 1
        return count


s = Solution()
ss = s.minLengthAfterRemovals(
    [1, 1, 1, 1, 1, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7])
print(ss)
ss = s.minLengthAfterRemovals(
    [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8,
     8, 9, 9, 9, 9, 10, 10])
print(ss)
ss = s.minLengthAfterRemovals([1, 3, 4, 9])
print(ss)
ss = s.minLengthAfterRemovals([1, 2, 3])
print(ss)

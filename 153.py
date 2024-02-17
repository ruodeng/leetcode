from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid
        return nums[i]
s = Solution()
ss = s.findMin([3,4,5,1,2])
print(ss)
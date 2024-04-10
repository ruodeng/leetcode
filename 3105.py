from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increaCount, decreasCount, maxCount=0,0,0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                increaCount += 1
                decreasCount = 0
            elif nums[i]<nums[i-1]:
                decreasCount += 1
                increaCount = 0
            else:
                increaCount = 0
                decreasCount = 0
            maxCount = max(maxCount,increaCount,decreasCount)
        return maxCount+1


s = Solution()
print(s.longestMonotonicSubarray([1,2,3,4,5]))
print(s.longestMonotonicSubarray([5,4,3,2,1]))
print(s.longestMonotonicSubarray([3,3,3]))
print(s.longestMonotonicSubarray([1,4,3,3,2]))

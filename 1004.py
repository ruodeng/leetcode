from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        for i, num in enumerate(nums):
            k -= 1 - num
            if k < 0:
                k += 1 - nums[l]
                l += 1
            else:
                res = max(res, i - l + 1)
        return res

s = Solution()
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
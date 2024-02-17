from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0, len(nums),2 ):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums

s = Solution()
ss = s.numberGame([1,2,3,4])


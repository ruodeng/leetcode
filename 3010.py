from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums.pop(0)
        nums.sort()
        return first+nums[0]+nums[2]

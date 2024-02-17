from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for i in range( len(nums)):
            if nums[i] <= k and not nums[i] in nums[i+1:]:
                return  len(nums)-i
        return 0



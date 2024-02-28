from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_sum = nums[0]
        for i in range(len(nums)):
            if nums[i] > max_sum:
                max_sum = nums[i]
        if max_sum < 0:
            return max_sum
        max_sum = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                max_sum += nums[i]
        return max_sum

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start=False
        for i in range(len(nums)-1):
            if nums[i] < nums[i + 1]:
                start=True
            if (start or i ==0) and nums[i] > nums[i+1]:
                return i
        return len(nums)-1

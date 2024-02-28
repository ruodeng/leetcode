from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        length = len(nums)
        if length %2 == 1:
            return False
        nums.sort()
        for i in range(length-2):
            if nums[i] == nums[i+2]:
                return False
        return True


s = Solution()
print(s.isPossibleToSplit([1,1,2,2,3,4]))
print(s.isPossibleToSplit([1,1,1,1]))
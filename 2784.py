import collections
from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if not nums[i]==i+1:
        #         return False
        # if not nums[-1] == nums[-2]:
        #     return False
        # return True


        dicts = collections.Counter(nums)
        if len(dicts) == 1:
            return False
        if not len(dicts) == len(nums)-1:
            return False
        max_key = max(dicts.keys())
        min_key = min(dicts.keys())
        if not max_key == len(nums)-1 or  not min_key == 1 or  not dicts[max_key] == 2:
            return False
        return True

s = Solution()
print(s.isGood([1,2,3,4,5,6,7,8,9,10,10]))
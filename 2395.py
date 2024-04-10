from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n-1):
            nums[i] = nums[i+1]+nums[i]
            # if nums[i] in nums[:i]:
        #         return True
        # return False
        del nums[n-1]
        # remove repeated elements
        nums = list(set(nums))
        return len(nums) != n-1

s = Solution()
print(s.findSubarrays([1,2,3,4,5]))
print(s.findSubarrays([4,2,4]))

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums2 = []
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums2.append(0)
                i += 1
            else:
                count = 0
                for j in range(i, len(nums)):
                    if nums[j] == 0:
                        break
                    else:
                        count += 1
                nums2.append(count)
                i = j
                if j == len(nums) - 1:
                    break
        m = 0

        if len(nums2) == 1:
            return max(nums2[0] - 1, 0)
        for i in range(len(nums2)):
            s = 0
            if i == 0:
                s = nums2[1]
            elif i == len(nums2) - 1:
                s = nums2[-2]
            else:
                s = nums2[i - 1] + nums2[i + 1]
            if s > m:
                m = s
        return m


s = Solution()
# print(s.longestSubarray([1,1,0,0,1,1,1,0,1]))
# print(s.longestSubarray([1,1,1]))
print(s.longestSubarray([0]))

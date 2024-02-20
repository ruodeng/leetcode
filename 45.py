from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        i = length - 1
        count = 0
        while i > 0:
            for j in range(i):
                if j + nums[j] >= i:
                    i = j
                    count += 1
                    break
                j += 1
        return count


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))  # 2
print(s.jump([2, 3, 0, 1, 4]))  # 2
# print(s.jump([2, 1]))  # 1
print(s.jump([1, 3, 2]))  # 1

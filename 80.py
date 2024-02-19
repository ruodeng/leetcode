from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i, j, count, removes = 0, 1, 1, []

        def analyze():
            if count > 2:
                k = j - count + 2
                if k < j:
                    removes.append((k, j))

        while j < len(nums):
            if nums[i] == nums[j]:
                count += 1
                j += 1
            else:
                analyze()
                count, i = 1, j
                j = i + 1
        analyze()
        removes.reverse()
        for remove in removes:
            nums[remove[0]:remove[1]] = []
        return len(nums)


s = Solution()
print(s.removeDuplicates([1, 1, 2, 2, 2, 3]))  # 2

1, 1
# [0,0,1,1,1,1,2]
# i,j
# j-i>1
# nums[i], nums[j ]

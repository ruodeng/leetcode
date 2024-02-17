from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        res = []
        def dfs(path, res):
            if len(path) == length:
                res.append(path)
                return
            for i in range(length):
                if nums[i] in path:
                    continue
                dfs(path+[nums[i]], res)


        dfs([], res)
        return res

s = Solution()
ss = s.permute([1,2,3])
print(ss)

# 1,
# 2,3
# 3,2
#
# 2,
# 1,3
# 3,1
#
# 3,
# 1,2
# 2,1
#
# 1,1,2,2,3,3
# 2,3,1,3,1,2
# 3,2,3,1,2,1
#
# 1
# 2,3

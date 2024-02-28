from typing import List


class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:

        def dfs(changeIndices, nums):
            pass

        marks = []
        for n in range(1, len(nums)+1):
            if n not in changeIndices:
                return -1
            else:
                # find all n's indexs in changeIndices
                marks.append([i for i, x in enumerate(changeIndices) if x == n])
                print(marks)


s = Solution()
s.earliestSecondToMarkIndices([1,3],[1,1,1,2,1,1,1])
    # def dfs(nums_in_dfs,index, s):
        #     #1 doing nothing
        #     dfs(nums_in_dfs, index+1,s)
        #     # 2 decrementing the number at nums_in_dfs
        #     if index == len(changeIndices):
        #         return s
        #     for i in range(len(nums_in_dfs)):
        #         if nums_in_dfs[i] == 0:
        #             continue
        #         else:
        #             dfs(nums_in_dfs[:i].append(nums_in_dfs[i]-1).extend(nums_in_dfs[i+1:]), index+1,s+1)
        #     # mark the index
        #     # can_mark = False
        #     for i in range(len(nums)):
        #         if nums[i] == changeIndices[index]:
        #             # can_mark = True
        #             dfs(nums_in_dfs[:i].append(nums_in_dfs[i]-1).extend(nums_in_dfs[i+1:]), index+1,s+1)


            
            # if index == len(changeIndices):
            #     return s
            # if nums[changeIndices[index]] == 0:
            #     return dfs(nums, changeIndices, index+1, s)
            # nums[changeIndices[index]] -= 1
            # s = min(s, dfs(nums, changeIndices, index, s+1))
            # nums[changeIndices[index]] += 1
            # return s

        # print(nums)
        # if nums[0] == 0 and not changeIndices[0] == 0:
        #     return -1
        # s = sum(nums)
        # if s +len(nums) >len(changeIndices):
        #     return -1
        # self.earliestSecondToMarkIndices(nums[:-1], changeIndices)
        # 
        # for ci in changeIndices:
        #     nums[k]-=1
        #     pass
        #     ci==index of nums







# nums = [2,2,0], changeIndices = [2,2,2,2,3,2,2,1]
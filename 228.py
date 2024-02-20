from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i=0
        res=[]
        while i < len(nums):
            j = i+1
            while j < len(nums):
                if nums[j]-nums[j-1]!=1:
                    break
                j+=1
            res.append(str(nums[i]) if i==j-1 else str(nums[i])+'->'+str(nums[j-1]))
            i=j
        return res
s= Solution()
print(s.summaryRanges([0,1,2,4,5,7]))  # ["0->2","4->5","7"]
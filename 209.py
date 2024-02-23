from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        t,i,j,m=nums[0],0,1,length+1
        nums.append(0)
        while j < length+1   :
            if t >= target:
                t-=nums[i]
                m = min(m,j-i)
                i+=1
            else:
                t+=nums[j]
                j+=1
        return 0 if m > length else m
s = Solution()
print(s.minSubArrayLen(7,[2,3,1,2,4,3]))  # 2
print(s.minSubArrayLen(4,[1,4,4]))  # 1
print(s.minSubArrayLen(11,[1,1,1,1,1,1,1,1]))  # 0

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length,left,right =len(nums), [1],[1]
        for i in range(1,length   ):
            left.append(left[i-1]*nums[i-1])
            right.append(right[-1]*nums[-i])
        for i in range(length):
            nums[i]=left[i]*right[length-i-1]
        return nums
s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))  # [24,12,8,6]



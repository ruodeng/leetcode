from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        i,j = 0,0
        temp = -1
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                temp = nums1[i]
                break
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        temp2 = int(str(nums2[0])+str(nums1[0]))
        if nums1[0] < nums2[0]:
            temp2= int(str(nums1[0])+str(nums2[0]))
        if temp == -1:
            return temp2
        return min(temp, temp2)
s = Solution()
# print(s.minNumber([4,1,3],[5,7]))
print(s.minNumber([6,4,3,7,2,1,8,5],[6,8,5,3,1,7,4,2]))
from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1,arr2,into_arr1=[],[],True

        for i in range(len(nums) ):
            # if switch:
            #     arr1.append(nums[i])
            #     switch = False
            # else:
            #     arr2.append(nums[i])
            #     switch = True


            if i %2 == 0:
                into_arr1 = True
                if len(arr1) > 0 and len(arr2) > 0:
                    if arr1[-1] < arr2[-1]:
                        into_arr1 = False

            else:
                into_arr1 = False
                if len(arr1) > 0 and len(arr2) > 0:
                    if arr2[-1] < arr1[-1]:
                        into_arr1 = True
            if into_arr1:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1+arr2
s = Solution()
ss = s.resultArray([2,1,3])
print(ss)

ss = s.resultArray([5,4,3,8])
print(ss)


from typing import List


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        # 1, (1)
        # 4, (1, 2)
        # 16, (1, 2, 4)
        # 3, 4
        # 3 ^ 2(3)
        # 4 ^ 2(3 + 4)
        #
        # 1,2,4
        #
        # 1
        # 1,2,4
        # 2
        # 2,4
        # 4
        # 4
        #
        # 1,2,4
        # 1
        #
        # 1,(1)
        # 2x2, (1, 2)
        # 4x4, (1, 2, 4),(1)

        # 1 ** 2, (1), (2, 3, 4, 5), (3, 4, 5), (4, 5), (5)
        # 2 ** 2, (2), (3, 4, 5), (4, 5), (5)
        # 3 ** 2, (3), (4, 5), (5)
        # 4 ** 2, (4), (5)
        # 5 ** 2, (5)

        1 **2, 1
        2 **2, 1,2
        4 **2, 1,1,2,4
        nums.sort()

        total = 0
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i+1, len(nums)):
                temp += nums[j]*j
            total += temp*nums[i]**2

        return total



        # total = 0
        # res = 0
        # for i in range(1,len(nums)+1):
        #     print('>><<',i, nums[:i], nums[i-1])
        #     total += nums[i-1]
        #     print(total,  nums[i-1]**2, total*nums[i-1]**2)
        #     if i >2:
        #         print(nums[:i-2])
        #         res += sum(nums[:i-2])*nums[i-1]**2
        #     res += total*nums[i-1]**2
        # # res+= nums[-1]**2
        # return res
s = Solution()
# print(s.sumOfPower([3,4]))
print(s.sumOfPower([2,1,4]))
# print(s.sumOfPower([76,24,96,82,97]))  #139...
# print(s.sumOfPower([1,1,1]))
# print(s.sumOfPower([1,2,3,4,5,6,7,8,9,10]))





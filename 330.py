from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        numLength= len(nums)
        i,j=0,0
        count =0
        # def check():
        #     for i in range(1, n+1):
        #         if i in nums or i == sum(nums):
        #             pass
        #         else:
        #             nums.append(i)
        #             count+= 1
        res=[]
        maxSum = 0
        for nn in range(1, n+1):
            print(nn, end=',',)
            found = False
            while i < numLength and   nn >= nums[i] :
                maxSum += nums[i]
                if nn == nums[i]:
                    found = True
                    j =i
                    break
                i+= 1
            if not found:
                print('not found num:', nn )
                print(nums[:j], res)
                if nn  <=2 or nums[j] + 1  < nn:
                    res.append(nn)
                    count+= 1

        print(res, count)
        return count



            # if nn in nums or nn == sum(nums):
            #     print('in')
            # else:
            #     nums.append(nn)
            #     count+= 1
            #     print('not in')

1,2,2=5
1+1+2+2
1,2,2


1,3
6
1,

# 10
# 1,5
# 4, 2,2
#
#
# 10,5,4
#
# 4,5,10
#
# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
# 0,1,0,1,0,0,0,0,0,10,
# 1,2,3,4
#
# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
# 0,1,0,1,1
# 1,3,3,7,12,22
#
# 1,2,3
# 0,0,0
# 1,3,5
#
# 1,2,3
# 0,1,0
# 1,3,6
#
# 1,

1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20


s = Solution()
ss = s.minPatches([1,3], 6)



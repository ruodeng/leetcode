from typing import List


# nums = [10,5,2,6], k = 100
# [10,5,2,6]


class Solution:
    # def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    #
    #     def check(nums, k):
    #         total_mul = 1
    #         for i in range(len(nums)):
    #             total_mul *= nums[i]
    #             if total_mul >= k:
    #                 return False
    #         return total_mul < k
    #
    #     length = len(nums)
    #     count = 0
    #     for i in range(length):
    #         for j in range(i+1):
    #             # print(j,length-i, nums[j:length-i+j],check(nums[j:length-i+j], k))
    #             if check(nums[j:length-i+j], k):
    #                 count +=1
    #
    #     return count
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        indexs = []
        for i in range(len(nums)):
            mul = 1
            right = 0
            for j in range(i, len(nums)):
                mul *= nums[j]
                if mul >= k:
                    right = j
                    break
                else:
                    right = j+1

            # print(i,right, nums[i:right])
            # [(0, 1), (1, 3)]
            indexs.append((i, right))
            if right == len(nums) :
                break
        # print(indexs)
        total = 0
        for i in range(len(indexs)):


            count = indexs[i][1] - indexs[i][0]
            n = (count + 1) * count // 2
            # # remove repeat
            repeat_count = 0
            if i < len(indexs) - 1:
                repeat_count=    indexs[i][1] -indexs[i + 1][0]
            m = (repeat_count + 1) * repeat_count // 2
            total +=n-m
            # print(indexs[i], nums[indexs[i][0]:indexs[i][1]] )
            # print('>>>>', count, n , repeat_count, m, n - m, total)
        return total




            # for j in range(i + 1, len(indexs)):
            #     if indexs[i][1] <= indexs[j][0]:
            #         print(indexs[i], indexs[j])


s = Solution()
ss = s.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
print(ss)
# ss = s.numSubarrayProductLessThanK([10,9,10,4,3,8,3,3,6,2,10,10,9,3], 19)
# print(ss)
# ss=s.numSubarrayProductLessThanK([7,10,3,2,32,5,7,1,33,2,16,14,10,5,25,21,1,27,9,31,9,26,11,17,16,5,21,11,27,3,21,4,20,29,26,12,22,30,18,30,19,14,21,2,28,21,25,23,4,6,12,27,26,3,28,25,9,26,18,15,2,20,28,31,32,24,19,6,6,20,6,4,11,8,32,31,25,31,25,4,4,17,17,16,16,32,19,31,13,13,24,28,32,32,28,13,33,11,11,29,9,29,7,12,8,1,12,27,11,23,14,1,8,14,28,21,25,20,32,31,30,27,20,22,27,7,18,3,14,30,4,21,12,23,11,10,5,19,2,15,10,6,26,5,32,8,11,33,16,25,28,17,15,2,9,13,16,4,26,10,18,20,22,30,30,24,16,17,1,12,27,27,28,1,20,27,17,20,31,1,25,10,15,18,7,25,12,33,15,9,27,30,9,15,27,24,32,20,8,9,13,15,20,20,16,7,1,24,25,32,28,14,12,24,33,8,11,30,26,14,17,17,23,24,9,14,3,2,33,29,10,4,13,25,14,24,32,26,26,27,17,15,13,19,32,28,25,31,13,1,3,9,33,19,1,11,5,1,7,16,11,8,29,23,25,9,14,16,20,32,25,3,17,7,8,12,15,13,18,28,30,7,24,7,20,26,32,16,9,27,31,27,2,24,29,1,6,21,19,32,22,1,29,29,21,33,32,13,1,17,31,19,18,31,13,5,18,2,30,9,31,32,22,4,7,10,1,21,19,19,2,29,31,16,19,32,14,24,19,30,4,4,27,28,25,28,20,3,8,3,19,16,7,6,31,19,13,19,4,23,30,30,26,20,33,10,1,20,27,23,6,19,10,9,3,32,27,7,5,14,27,7,17,7,13,20,16,32,4,30,9,33,6,28,9,26,23,24,23,6,19,32,28,11,18,16,15,1,23,19,5,4,17,18,22,11,14,31,33,5,22,4,10,22,12,3,4,16,25,26,31,13,30,32,19,12,11,24,32,12,9,17,21,3,5,10,4,19,5,27,7,16,3,11,24,28,20,15,22,14,8,1,26,15,29,32,8,25,30,29,31,4,31,15,28,26,26,18,9,21,12,16,30,18,6,32,3,33,11,20,23,17,26,22,14,19,7,29,6,10,1,18,32,11,1,23,4,12,18,6,26,18,3,27,17,33,27,21,6,23,5,3,20,4,24,13,10,29,30,19,11,32,3,9,1,30,28,24,25,6,18,17,16,24,3,16,12,20,2,19,2,15,30,7,31,20,33,25,14,4,14,26,18,4,16,2,33,10,31,19,6,22,16,25,26,9,33,23,26,26,21,26,24,22,10,33,22,9,27,3,32,7,1,2,10,26,2,16,6,10,4,12,10,31,27,9,26,31,21,20,4,33,14,6,6,27,13,30,20,1,28,17,7,32,9,8,8,30,15,9,28,10,7,15,28,30,24,7,16,23,18,20,6,15,2,10,13,9,21,13,30,27,4,31,31,2,32,6,12,31,26,29,22,10,27,19,14,13,7,30,33,8,16,16,7,1,7,30,21,26,2,27,25,22,8,27,6,1,33,13,24,12,14,25,31,6,24,16,2,28,29,7,12,2,32,22,30,11,7,24,31,15,15,13,4,12,8,7,24,3,13,21,17,2,18,11,5,21,23,31,8,23,4,15,10,12,31,24,13,4,7,12,33,10,11,13,13,24,11,24,32,22,13,9,26,26,15,7,19,26,14,21,33,32,23,26,15,33,28,7,20,1,33,13,13,11,25,29,30,25,12,31,6,16,21,23,6,23,33,3,17,17,19,1,33,1,5,24,28,4,19,16,7,12,16,23,24,19,3,2,23,24,32,32,26,19,11,8,31,5,12,33,1,19,11,16,1,2,18,10,26,5,15,18,12,4,11,10,29,31,33,26,9,28,3,9,7,15,11,5,28,5,32,32,27,12,20,1,12,16,19,22,3,21,10,12,30,3,11,12,17,1,24,19,3,30,25,17,31,8,4,4,29,25,2,30,25,20,28,22,23,26,16,2,18,27,28,30,32,1,24,7,15,30,7,9,29,4,15,11,11,15,19,18,15,33,2,20,5,10,1,31,4,30,16,17,32,12,6,32,20,31,18,6,21,4,11,2,29,30,15,8,32,8,5,9,21,13,33,4,3,1,17,13,18,24,13,30,14,17,4,2,26,22,1,17,17,21,21,19,16,11,32,31,9,33,2,4,33,19,11,33,6,8,33,32,30,20,2,6,2,14,26,7,6,18,30,11,14,5,16,14,30,12,7,20,28,12,11,25,21,3,21,25,10,1,32,6,29,12,2,6,5,15,8,15,2,20,28,3,6,26,8,33,6,23,1,13,13,3,29,7,10,32,6,20,12,33,12,12,30,4,7,31,16,16,6,30,5,18,18,26,3,19,1,11,30,1,10,3,19,25,26,31,26,14,25,20,18,27,32,6,30,21,8,2,13,18,7,30,12,15,8,17,3,28,21,9,32,3,29,2,4,32,25,26,11,22,15,2,2,13,30,7,31,7,18,31,24,17,16,16,22,5,12,7,21,4,14,1,20,18,16,10,20,13,19,14,3,19,12,1,6,13,17,28,19,17,23,29,18,26,9,24,20,1,31,26,31,16,24,25,9,13,31,14,14,22,14,10,24,14,31,26,11,20,27,10,20,1,17,7,3,17,29,25,32,20,14,19,32,9,7,12,28,25,10,5,18,6,1,10,6,17,16,33,27,21,31,8,29,23,32,14,23,9,2,27,27,4,8,7,31,12,16,13,31,6,19,4,23,3,10,9,30,16,19,11,33,12,23,22,18,1,15,17,10,23,28,22,8,4,14,18,31,11,26,11,29,21,19,4,9,16,20,14,17,20,10,21,8,2,10,13,10,33,14,24,32,9,6,8,9,25,18,16,19,18,18,13,12,17,19,29,12,32,27,29,19,15,17,16,11,17,18,29,9,24,27,17,27,3,24,31,23,27,23,14,1,1,30,15,8,9,15,6,13,30,13,26,1,20,1,22,1,21,8,15,11,15,27,12,24,5,14,8,7,12,20,18,31,28,1,31,7,3,18,23,12,15,9,12,33,12,25,7,33,15,16,10,15,10,1,5,18,2,5,9,29,2,9,15,2,9,18,13,27,8,5,4,6,21,32,14,22,13,9,14,21,33,24,4,16,31,16,4,4,7,14,23,5,20,20,1,23,18,19,19,1,33,21,24,8,7,12,13,20,25,5,27,6,29,16,19,33,2,12,2,10,10,8,19,27,1,25,32,28,3,9,27,31,9,15,7,23,7,2,3,11,2,16,2,14,30,19,27,23,8,11,6,1,31,7,13,5,4,33,29,8,26,24,12,6,4,4,32,4,25,10,17,8,24,24,27,18,10,29,25,10,21,26,33,22,20,25,4,11,16,9,17,30,3,2,14,30,25,4,28,20,6,1,16,27,20,6,29,8,31,28,31,7,15,31,1,17,7,18,33,24,12,1,22,11,9,24,6,18,9,26,26,11,32,22,29,6,3,15,23,21,20,24,19,31,29,13,25,4,23,30,7,14,23,2,21,9,5,10,3,21,8,1,1,18,10,8,32,22,23,29,7,15,24,3,27,3,20,7,33,18,33,16,3,15,11,4,11,22,5,14,26,19,25,21,25,33,2,8,14,10,32,9,21,29,5,3,22,20,28,33,2,17,29,8,16,25,3,19,6,14,15,22,13,6,31,32,24,12,10,7,2,14,25,20,30,33,33,31,4,22,24,17,16,16,10,21,22,23,10,19,7,6,33,28,29,13,29,8,19,26,20,8,7,6,1,30,23,26,9,7,18,30,6,12,10,33,15,24,20,30,20,1,10,6,25,4,24,12,16,15,15,23,18,17,1,8,4,21,20,29,24,27,4,3,24,7,8,24,9,26,25,14,15,27,15,6,29,31,9,15,2,18,16,17,1,17,6,27,8,21,18,14,12,1,33,2,12,32,4,26,15,17,1,33,28,30,13,25,8,2,13,30,20,3,13,16,6,21,6,33,31,12,31,33,5,17,14,2,28,17,19,8,21,21,26,25,3,9,12,20,15,2,15,23,17,12,11,4,22,32,18,24,23,25,6,30,22,25,16,30,11,21,11,2,17,18,24,3,18,27,20,11,3,32,19,30,6,1,2,5,5,16,13,30,2,2,15,7,15,4,31,16,25,30,32,9,24,26,10,28,32,21,1,16,17,9,32,23,10,18,24,3,26,31,3,18,20,22,14,28,29,15,6,1,16,16,32,14,19,28,4,33,11,31,13,27,25,30,4,24,1,16,1,24,8,14,4,29,29,7,7,25,2,22,16,1,8,19,22,1,7,25,14,16,32,28,1,6,15,11,12,5,11,10,31,25,8,8,24,12,2,18,3,5,19,32,6,5,24,16,24,16,28,22,13,14,32,7,14,9,11,26,18,10,17,8,22,13,22,5,1,17,28,8,12,2,25,27,20,15,20,28,12,23,32,15,15,30,30,9,17,6,31,4,9,19,6,24,33,27,23,33,33,33,27,29,28,30,8,16,5,22,23,31,30,6,33,23,13,14,7,6,9,13,6,8,33,20,17,24,3,26,15,19,12,19,11,28,13,27,31,25,27,21,19,29,18,28,11,19,17,9,13,21,1,25,30,27,19,2,25,18,18,11,12,2,5,27,11,2,20,5,28,7,5,31,1,18,17,31,14,26,30,29,26,30,23,30,16,31,8,2,27,19,12,13,21,6,4,9,14,4,8,25,2,20,11,7,4,10,22,18,28,2,19,14,3,17,4,31,9,20,33,13,11,13,13,22,2,1,26,7,19,32,27,31,5,22,24,11,23,10,17,26,32,31,8,17,6,1,32,16,28,8,15,15,19,7,21,27,27,25,27,18,18,33,33,11,11,33,15,7,11,17,30,25,32,20,11,26,33,5,32,30,19,16,13,30,24,20,22,21,4,1,28,4,1,30,16,23,31,7,32,32,19,25,1,18,12,19,15,31,22,2,14,28,11,19,22,9,3,1,4,22,15,10,5,26,24,16,30,5,17,25,32,8,9,11,32,5,9,29,3,13,17,29,24,27,21,18,25,13,19,23,8,1,10,22,1,30,9,26,29,12,5,20,32,30,23,13,9,26,4,16,32,6,2,17,28,9,31,7,13,22,7,27,10,17,16,4,10,2,30,26,32,9,26,3,31,15,14,21,11,27,11,18,17,24,1,22,25,31,23,33,22,20,27,6,6,15,3,4,25,17,3,5,16,27,33,28,18,15,7,18,13,9,25,30,13,1,4,9,9,14,11,13,8,30,24,21,31,7,33,13,29,7,23,10,25,8,31,13,30,12,23,22,29,7,8,8,20,31,23,15,22,14,15,6,11,7,2,15,17,22,12,17,2,15,3,12,17,23,24,24,5,15,2,31,33,19,26,30,25,13,25,31,1,13,10,24,8,23,10,17,1,14,22,20,9,4,21,14,15,23,27,7,17,14,14,13,6,26,13,9,8,9,29,7,25,16,24,6,10,1,8,8,15,2,19,4,26,12,9,14,8,32,31,23,13,24,2,6,15,14,16,12,15,3,1,32,30,14,32,15,3,5,7,13,23,33,13,18,26,8,8,28,1,27,1,7,11,1,32,18,32,10,11,20,8,33,30,20,9,17,23,17,27,22,21,22,29,3,20,18,22,22,30,29,24,23,17,17,31,13,8,31,20,19,1,5,23,21,6,10,15,17,29,6,30,9,24,24,1,14,11,32,8,9,12,21,23,26,23,10,26,24,26,15,26,29,29,31,8,20,8,30,9,23,20,23,12,23,7,6,17,1,18,22,7,6,30,13,2,15,11,29,4,16,20,16,27,29,27,8,13,33,19,29,22,21,16,26,31,12,4,30,27,7,12,12,9,2,5,32,3,20,30,14,28,2,22,32,20,9,19,13,23,6,12,13,23,27,1,4,16,25,10,16,19,32,31,25,25,5,3,15,23,5,8,25,32,6,25,10,30,2,19,31,17,27,20,18,2,24,3,15,8,27,28,12,6,30,20,21,28,12,23,10,28,14,30,24,19,28,23,33,29,22,8,23,13,11,4,10,22,33,2,10,18,12,3,1,14,3,33,31,6,14,12,8,12,29,6,28,12,27,26,1,30,21,25,8,27,20,12,1,11,11,18,7,18,1,8,10,12,33,10,15,17,31,7,28,9,18,21,23,30,25,11,1,31,22,16,6,24,17,13,33,6,8,16,32,4,5,26,4,6,25,12,26,7,13,16,33,18,29,11,32,5,19,30,27,25,6,31,32,19,18,2,14,21,8,28,17,16,24,15,1,6,23,26,2,6,16,12,29,15,16,3,6,4,7,25,3,10,31,15,4,5,16,25,10,24,29,29,1,2,33,13,29,7,30,20,15,10,4,21,26,30,14,23,18,1,32,30,32,4,23,25,20,12,2,6,15,7,17,26,13,18,1,32,25,30,21,22,26,2,2,12,27,6,8,23,26,22,7,32,31,24,27,10,28,21,28,31,21,15,16,30,16,31,7,10,4,32,26,22,26,2,18,17,23,6,17,15,16,29,23,29,31,8,19,8,30,5,19,27,24,7,13,3,22,32,12,6,29,19,21,10,9,22,19,16,9,30,9,7,28,14,3,25,19,13,2,29,2,28,24,8,10,27,2,32,17,13,3,22,29,26,28,7,33,30,32,23,20,32,6,14,17,20,25,5,22,8,1,12,27,14,12,32,14,30,33,18,28,17,2,2,33,29,23,30,2,27,8,1,18,7,15,18,32,31,2,32,20,33,25,24,31,19,22,16,6,11,8,32,15,17,2,4,11,17,27,16,30,25,18,27,21,17,16,30,33,1,10,23,22,1,31,1,8,8,14,19,25,9,21,23,11,5,10,31,26,25,3,32,24,27,30,2,21,33,5,2,31,15,12,30,13,27,29,11,31,21,29,28,29,24,15,23,28,16,31,18,29,9,17,20,10,15,30,19,11,2,7,29,10,22,17,18,1,6,4,20,11,8,1,6,9,28,17,33,28,27,9,32,1,1,17,17,32,31,18,27,1,18,28,32,22,21,32,18,19,19,27,29,15,28,30,33,9,13,33,22,7,21,32,20,33,33,14,7,25,1,22,1,31,7,32,9,10,10,32,13,23,17,19,32,27,22,7,11,1,19,24,17,14,24,6,4,18,24,9,12,6,17,18,11,16,10,4,13,5,23,31,11,8,29,5,32,19,32,10,3,29,15,18,17,21,7,24,12,24,3,26,1,3,7,5,17,23,2,15,19,23,10,12,27,22,28,33,5,22,2,1,27,13,15,9,10,12,4,19,30,5,21,2,31,13,3,32,7,9,18,27,11,14,30,27,21,14,17,27,15,5,8,30,32,25,23,17,22,2,6,7,33,25,26,26,8,31,12,7,30,12,10,31,26,10,33,24,18,18,4,5,25,28,2,2,19,16,24,10,32,5,18,18,33,9,13,6,22,14,3,18,21,16,29,2,2,20,7,31,17,12,9,12,30,15,20,3,18,24,3,9,9,3,15,6,7,18,6,30,29,12,2,23,23,13,9,9,29,21,13,24,22,32,11,27,29,9,15,18,6,22,9,14,7,31,7,19,22,25,8,31,26,2,2,20,13,7,18,20,2,3,4,3,19,30,13,28,2,5,18,23,20,12,28,22,9,15,33,30,5,26,18,5,31,29,12,20,16,16,10,17,28,15,7,32,20,4,20,3,20,18,29,28,23,15,8,29,13,18,6,5,25,19,12,30,6,28,4,15,11,11,21,16,6,1,22,10,20,21,33,2,20,13,25,24,30,3,29,28,16,10,9,19,1,32,28,11,18,26,17,20,16,2,14,27,28,20,12,17,31,2,22,2,22,24,24,32,7,19,22,1,4,13,24,17,23,27,20,2,2,25,2,26,19,16,1,9,11,5,12,9,20,11,33,13,23,28,13,13,23,9,32,32,8,3,26,14,1,22,17,12,27,29,12,5,26,5,26,2,4,25,33,23,2,22,4,17,33,8,31,14,25,26,12,19,31,24,17,7,31,29,6,8,15,12,11,5,11,24,2,4,27,14,11,7,28,9,20,19,29,4,5,13,28,14,20,23,27,17,4,27,18,22,3,18,18,17,11,3,6,33,31,15,28,5,31,16,31,15,25,32,24,4,11,29,5,1,22,1,12,31,7,28,6,6,13,23,28,26,31,7,31,14,17,12,15,10,8,20,4,15,11,21,29,5,4,8,6,16,18,9,12,14,2,6,18,13,23,2,29,32,13,28,27,31,31,6,26,17,10,4,21,7,24,6,5,24,14,8,25,13,17,23,25,13,14,25,6,16,32,10,26,3,16,30,4,21,16,31,28,31,9,8,29,16,19,7,8,14,23,21,13,3,4,22,20,10,10,14,29,25,30,14,10,3,2,26,30,23,4,14,10,27,16,20,25,7,17,12,8,21,17,7,32,11,11,1,28,12,16,12,7,30,8,11,23,4,8,25,11,2,21,33,4,15,9,17,16,4,22,14,7,21,19,7,28,3,24,33,14,25,9,4,9,13,27,6,16,26,32,13,3,21,20,9,17,13,23,11,23,30,10,17,1,27,14,16,6,14,27,10,22,21,31,31,33,27,15,8,10,30,25,28,1,26,29,30,23,18,26,9,24,13,4,1,33,33,30,28,7,23,17,22,33,13,32,1,29,21,19,22,32,30,19,20,30,33,13,19,9,7,26,18,31,14,8,32,24,30,17,18,29,6,18,20,4,18,15,10,16,15,14,10,32,29,33,31,21,32,1,15,18,29,27,13,21,4,30,12,8,27,4,8,31,22,28,12,5,22,9,8,12,21,14,18,12,27,12,9,29,31,11,6,5,10,2,10,6,10,4,32,15,17,10,25,8,14,17,33,1,2,21,7,21,5,9,12,9,2,26,1,18,14,7,11,20,2,23,13,27,29,23,2,13,11,26,4,18,26,27,6,6,29,1,16,15,1,25,2,4,23,14,19,30,21,27,25,6,17,18,15,25,17,26,3,14,16,1,28,33,10,11,3,31,1,23,33,18,18,25,23,22,11,26,8,19,18,10,9,32,10,30,4,6,29,10,24,21,22,26,33,25,10,4,19,9,19,7,30,7,26,33,24,3,24,18,7,23,18,17,13,30,13,14,10,17,21,7,5,32,12,8,18,29,21,12,16,1,33,10,17,22,29,26,7,18,19,14,4,25,10,3,6,8,4,31,13,14,16,11,3,3,27,11,23,2,13,31,1,10,23,22,6,11,27,21,27,3,31,19,20,2,33,29,17,3,12,18,1,14,19,3,30,11,22,6,16,22,26,16,19,23,33,2,11,12,22,13,4,9,27,23,29,30,32,27,2,6,6,17,31,3,4,4,17,7,27,25,26,2,28,1,18,25,27,21,2,26,18,27,10,15,9,13,2,2,2,23,33,15,1,30,14,22,25,25,26,25,22,12,19,7,33,24,24,12,14,17,17,29,21,11,17,20,10,23,2,14,12,30,20,22,33,11,15,33,29,32,27,12,15,11,19,32,26,14,32,25,11,18,6,27,2,3,16,23,29,21,23,11,22,14,27,18,28,10,3,1,33,25,23,29,19,2,31,24,25,27,10,9,14,27,16,9,33,25,30,25,18,16,3,2,33,25,7,19,16,5,14,13,2,5,3,32,9,33,31,2,25,4,22,9,33,4,9,6,17,1,31,25,12,14,28,22,10,16,3,22,26,23,33,15,22,7,29,8,14,31,14,19,7,27,29,13,32,20,16,5,13,9,5,17,15,22,28,27,24,12,21,15,33,28,22,25,33,7,18,6,10,33,33,22,28,31,6,21,18,15,29,20,33,18,25,5,7,4,1,25,1,23,21,30,23,26,30,21,4,28,16,33,15,24,12,2,20,11,5,30,4,31,12,12,27,29,9,16,23,6,6,30,19,25,33,10,32,32,26,9,11,17,32,8,20,33,5,24,24,14,1,11,14,2,29,15,7,7,10,27,9,33,19,10,17,33,12,28,11,3,33,18,19,26,19,11,7,25,33,11,9,7,14,11,32,19,5,3,25,27,22,5,32,16,8,8,20,6,7,14,8,30,11,19,19,4,5,10,21,32,13,7,8,8,11,29,11,10,18,6,19,22,7,27,7,5,8,22,33,14,14,15,26,14,14,14,14,22,32,2,5,26,27,22,9,32,22,32,18,20,11,1,11,18,28,9,20,15,13,32,5,22,27,15,9,2,12,11,20,11,32,20,12,18,12,10,13,31,27,7,22,26,1,16,17,12,9,23,21,9,23,20,13,25,33,11,5,12,17,15,2,30,12,2,7,12,6,18,8,31,23,1,10,23,28,12,32,25,17,11,33,30,3,2,20,19,11,2,8,25,3,23,15,31,24,12,28,31,18,23,27,19,5,10,29,25,8,31,5,32,1,4,8,6,21,28,4,10,25,14,6,12,11,21,33,28,32,27,30,31,18,8,14,11,25,30,20,25,2,28,30,33,22,12,24,7,24,21,8,10,12,20,11,5,9,20,7,12,14,31,33,9,19,4,20,25,29,27,32,15,24,23,14,19,11,6,13,31,22,22,16,21,7,17,24,20,2,18,15,5,19,13,24,20,12,18,12,15,9,30,22,12,3,23,10,26,20,30,18,32,31,2,22,28,28,19,27,23,24,32,23,29,21,21,17,23,3,28,10,19,17,22,30,6,18,16,14,31,17,3,23,7,22,30,20,11,33,25,6,8,11,28,25,9,31,17,24,26,26,30,11,14,7,19,28,17,30,29,26,24,6,7,27,26,30,6,7,22,15,8,10,10,28,28,19,11,23,9,26,24,3,9,6,12,17,10,16,14,1,20,4,17,19,22,30,20,9,11,29,21,22,17,28,29,17,24,5,21,33,22,19,6,32,11,8,20,1,27,23,11,28,32,12,9,4,29,16,1,17,7,33,5,30,21,30,26,21,15,13,11,1,2,29,20,32,27,3,11,3,27,21,8,18,14,18,1,25,24,30,15,14,6,7,2,33,14,24,23,30,11,20,9,10,2,26,32,25,30,15,33,24,9,21,30,23,23,5,27,16,33,22,5,4,27,17,12,24,4,20,26,14,3,2,5,22,5,2,27,4,9,28,21,26,3,13,6,33,18,27,9,5,3,32,7,13,28,19,11,4,11,23,3,24,12,18,17,22,3,30,33,20,8,19,1,24,16,2,33,31,21,5,14,1,32,16,29,32,27,30,31,8,4,16,32,22,27,2,21,27,26,13,9,15,8,15,16,16,21,27,33,16,21,4,24,32,16,21,17,23,22,13,18,15,18,7,12,10,4,10,19,21,5,25,18,20,24,14,10,3,11,32,4,31,15,22,17,10,31,21,11,33,1,21,2,31,9,25,23,10,15,21,25,24,14,4,32,3,9,28,33,32,19,31,5,5,22,20,7,9,15,14,2,17,6,31,31,30,25,10,7,16,16,21,2,27,13,1,17,29,26,20,11,13,33,20,4,15,10,3,1,29,32,28,17,17,21,26,23,33,23,32,4,25,28,4,14,9,22,3,15,29,30,13,29,26,16,31,21,33,14,9,29,10,15,12,24,13,10,24,26,3,17,1,4,18,24,16,25,3,19,20,19,22,27,23,11,31,22,24,13,33,7,27,20,26,31,21,21,8,3,16,7,17,4,13,19,16,2,3,18,18,33,7,18,11,5,13,12,25,17,18,26,32,26,17,21,20,29,26,19,25,12,20,33,1,31,9,32,30,5,12,12,28,18,10,32,17,32,14,17,31,30,10,16,33,33,31,33,3,28,14,27,13,26,30,21,1,2,23,25,8,21,17,7,19,20,11,32,20,8,26,29,8,27,12,14,19,6,14,21,25,3,12,8,25,7,28,32,22,32,32,16,29,5,4,24,5,3,22,20,32,30,3,25,12,13,32,29,30,20,27,14,17,21,15,12,16,16,3,16,27,29,21,33,27,7,33,28,26,23,8,15,20,21,8,26,28,15,19,25,17,19,17,30,32,2,9,16,23,12,30,10,17,31,17,20,27,20,25,16,32,27,27,28,19,27,23,7,33,3,2,13,26,17,7,19,31,12,21,7,7,9,25,15,27,2,31,11,7,12,9,3,29,13,30,32,17,33,26,7,5,2,2,29,28,33,29,9,16,23,28,12,5,27,4,20,22,17,22,1,28,14,5,19,1,20,30,2,5,20,22,23,13,6,27,13,2,9,22,21,28,29,24,11,30,15,4,7,2,19,21,33,13,28,17,4,8,8,2,6,29,10,20,4,20,22,33,15,16,32,15,19,25,27,21,13,2,32,4,3,32,2,14,24,33,16,29,7,16,2,26,16,25,33,31,18,7,16,14,12,32,25,9,32,14,29,19,12,4,24,13,11,26,7,28,12,28,9,1,13,31,13,22,20,16,6,7,2,29,33,29,13,21,9,2,3,16,31,31,1,33,5,29,4,28,19,11,16,10,20,18,1,10,27,26,15,26,3,30,16,20,32,25,32,16,12,29,27,10,26,12,27,11,30,29,8,6,11,18,14,7,22,24,10,11,4,32,24,33,20,29,15,25,22,17,7,2,2,17,27,17,2,30,17,27,27,26,16,32,1,8,17,33,16,24,2,18,8,7,17,26,30,16,33,25,8,18,17,12,33,1,9,6,23,13,25,3,10,7,17,23,16,7,14,21,13,3,5,8,1,17,4,26,11,9,32,30,1,11,31,1,30,13,21,11,13,26,16,28,6,33,23,8,26,1,21,25,31,14,9,6,23,6,25,28,20,7,14,5,13,22,30,28,28,31,21,1,18,32,3,11,23,8,27,22,11,10,29,21,12,33,1,26,1,2,32,33,15,9,28,20,26,1,22,25,26,15,1,24,33,23,8,6,27,32,15,17,2,21,32,21,6,23,4,26,24,5,18,11,6,26,18,30,28,32,17,16,13,9,1,14,31,12,2,26,33,21,13,10,8,7,7,20,1,31,19,17,13,14,28,18,8,27,22,33,18,8,7,19,8,24,29,7,30,13,28,28,18,18,27,24,11,17,26,5,25,14,5,3,13,20,8,2,29,32,13,5,27,13,12,16,27,16,23,19,11,20,26,30,31,22,22,25,13,29,10,3,30,23,7,27,29,5,28,8,20,4,1,31,26,31,21,15,20,15,24,32,16,20,3,31,21,23,27,26,5,14,9,21,7,15,33,18,11,7,27,3,29,33,29,30,4,22,30,18,25,19,10,7,15,15,9,21,26,22,25,10,32,27,6,8,19,19,15,25,3,16,2,24,8,22,3,4,19,14,11,21,24,26,4,13,19,13,8,9,4,15,23,20,27,7,31,33,18,23,8,19,22,2,23,32,23,16,33,1,14,24,30,1,22,9,19,20,33,29,19,18,1,22,10,3,9,11,25,10,16,20,29,17,19,32,33,18,5,13,21,20,12,4,28,8,9,16,5,6,18,15,14,33,21,4,11,1,8,6,5,9,24,32,14,26,7,3,8,23,31,3,21,8,8,5,23,7,4,2,23,24,1,9,33,21,5,10,15,12,25,21,25,31,12,25,25,31,28,27,2,33,18,15,31,33,15,5,23,3,28,12,33,32,24,23,24,15,6,25,29,25,2,17,16,26,23,6,5,18,22,4,12,8,27,33,16,23,32,6,17,23,4,21,3,24,2,23,3,28,1,4,12,20,18,22,4,24,28,25,21,31,30,18,32,3,3,26,22,6,14,16,18,1,11,16,24,20,14,22,5,17,17,10,19,2,13,20,16,27,5,14,32,3,10,27,15,31,27,8,27,10,6,25,2,11,8,14,10,4,24,26,2,33,22,23,3,22,6,7,14,10,25,20,20,9,25,23,20,12,14,32,30,3,14,24,6,9,9,23,11,29,23,7,3,18,30,1,8,9,13,1,1,19,22,33,20,13,6,10,31,26,25,25,17,23,31,7,15,27,26,15,18,21,28,8,18,10,16,21,17,8,14,11,16,14,24,21,13,23,1,27,20,11,32,15,11,6,24,17,27,1,8,8,8,15,6,4,30,21,16,31,7,8,7,30,1,18,10,18,5,33,21,23,20,19,22,19,30,24,33,7,20,2,8,29,30,30,14,3,30,2,16,27,32,9,17,22,29,18,5,22,10,9,8,21,23,27,2,3,27,22,16,26,6,7,22,7,30,8,12,4,7,19,28,21,29,15,10,19,5,23,7,24,18,23,32,18,11,22,15,14,8,13,22,12,28,23,9,10,28,15,16,23,26,31,29,28,5,12,8,26,30,21,19,26,32,8,20,15,25,14,6,25,16,16,19,7,31,7,5,19,7,10,19,3,4,2,30,22,22,10,17,23,22,24,32,6,6,28,25,3,12,9,5,4,13,20,25,22,2,18,17,27,30,27,6,26,29,31,15,5,12,20,20,5,22,3,7,21,28,2,2,25,31,1,22,22,12,14,25,14,20,6,25,25,25,7,2,24,26,15,11,14,16,31,27,32,31,30,18,14,18,10,31,29,33,28,20,3,14,14,24,2,18,8,15,21,3,22,29,32,5,3,21,27,24,11,13,21,2,6,26,6,10,4,27,1,3,14,4,17,13,20,33,6,28,9,19,16,17,9,10,15,17,13,3,2,32,14,28,14,26,9,9,22,12,16,9,14,9,33,33,18,17,19,33,21,22,5,21,7,5,7,28,22,29,26,26,24,29,12,1,29,16,28,25,18,13,21,27,6,26,28,10,21,29,18,1,4,20,33,14,17,10,27,19,17,28,19,17,30,24,18,1,22,27,3,17,23,25,31,11,6,24,3,29,1,7,6,33,23,4,7,28,5,11,14,31,7,28,13,3,3,25,22,29,2,2,15,4,5,32,27,31,31,32,27,28,22,32,33,19,24,4,14,7,9,9,6,23,27,10,19,15,8,14,4,8,13,26,24,31,12,12,28,8,28,25,22,25,28,3,29,15,30,17,17,2,9,29,24,2,29,16,2,3,9,13,16,8,11,25,4,18,26,31,16,21,1,17,4,14,15,32,17,2,20,22,28,16,12,26,7,28,15,23,9,9,18,17,12,29,14,16,3,15,16,20,28,14,29,16,20,7,25,9,4,10,2,5,29,19,1,26,16,30,14,10,27,22,12,6,29,15,24,33,18,9,16,22,24,2,26,17,19,9,21,22,8,22,12,21,13,28,12,27,32,23,5,17,16,28,14,23,22,26,30,16,14,12,6,18,21,20,33,15,4,21,33,32,8,6,20,12,27,11,27,18,7,14,26,12,2,28,21,19,33,28,23,12,6,5,2,4,31,6,4,16,15,13,12,26,28,33,15,2,18,31,18,19,6,28,10,33,13,27,25,16,18,22,16,27,32,27,4,16,5,11,5,29,26,6,7,18,18,12,22,17,1,23,5,13,17,8,12,19,26,24,25,8,21,4,6,4,27,26,19,15,31,4,4,6,25,16,15,12,31,2,32,1,10,20,2,14,4,21,17,32,1,16,5,15,9,1,6,30,28,9,3,27,2,13,3,19,18,1,28,2,24,18,8,28,24,30,23,22,5,15,1,32,29,14,6,22,29,8,4,26,30,20,9,22,15,8,7,28,25,8,18,5,28,6,31,1,29,25,9,18,16,19,11,7,30,13,7,8,27,14,20,22,10,1,32,24,17,21,14,28,16,32,12,23,6,5,32,11,30,24,31,27,32,4,5,15,12,13,2,29,17,9,13,20,21,4,29,17,13,19,4,8,2,29,13,23,32,24,17,4,7,12,1,6,23,8,3,4,30,32,27,19,10,11,8,22,9,16,1,22,2,32,6,10,23,5,27,8,3,21,13,3,12,31,24,28,28,16,2,19,4,33,29,15,11,7,7,8,9,26,11,14,13,17,14,29,27,29,8,10,31,27,1,13,15,12,2,8,6,12,16,20,6,33,12,12,8,28,9,12,33,26,16,9,17,31,24,13,9,33,27,14,28,11,15,32,14,21,18,12,1,18,1,29,6,1,3,23,30,19,19,27,14,10,30,24,33,33,7,25,21,32,3,8,16,31,23,6,11,21,12,33,6,11,4,33,20,25,21,2,9,2,21,9,3,1,24,27,4,2,27,13,23,24,28,4,17,17,20,33,21,33,14,22,5,29,10,14,19,24,23,31,13,25,23,25,16,21,4,15,8,33,31,2,23,15,30,14,5,32,12,21,24,5,26,1,10,13,2,15,13,4,27,18,7,16,26,26,10,2,16,31,2,13,13,33,33,2,23,8,8,6,27,7,12,28,4,2,26,20,15,8,17,21,29,5,12,14,8,17,22,9,18,6,13,22,3,8,13,31,3,21,8,5,33,21,18,19,11,30,31,15,30,5,4,21,4,21,9,8,27,19,2,15,5,19,10,33,19,24,13,20,1,17,19,22,5,1,14,6,16,21,28,4,12,12,6,31,2,33,17,16,12,16,18,24,3,14,22,4,31,3,27,30,7,4,21,28,17,23,28,8,26,17,14,5,20,10,10,8,28,14,31,30,27,16,24,3,8,32,16,11,12,28,13,32,28,25,12,6,32,14,25,1,5,18,21,16,23,14,27,18,4,6,1,20,7,15,33,28,9,30,12,31,6,6,20,31,3,8,19,16,6,4,8,11,29,25,3,33,27,9,11,30,3,28,21,32,32,14,17,32,15,5,24,25,12,15,24,9,22,24,7,17,22,24,25,22,31,6,14,5,14,15,23,22,32,11,23,20,6,5,26,17,22,17,1,25,26,27,7,3,3,1,7,19,13,21,32,24,28,4,19,7,3,25,20,18,32,11,16,31,5,12,15,33,6,11,26,24,13,28,31,30,8,20,23,29,6,18,7,19,25,4,24,25,11,27,19,17,4,12,23,26,33,30,24,24,26,7,13,11,26,11,1,14,1,10,1,27,21,16,14,16,8,21,3,23,22,8,4,19,16,30,11,23,4,25,23,11,21,25,27,7,18,22,20,32,20,32,30,16,4,28,16,23,28,24,10,28,4,6,26,24,19,6,1,12,4,15,5,22,17,13,20,30,22,10,13,19,13,22,5,17,15,4,12,12,24,9,1,19,29,12,19,31,18,27,29,24,28,7,31,28,3,8,29,27,29,25,5,3,30,5,23,27,30,30,33,19,2,16,18,33,20,3,22,27,25,21,23,13,30,18,3,23,18,8,9,20,7,6,3,13,20,10,19,32,23,13,32,17,10,1,20,22,3,2,14,14,6,8,11,31,23,25,4,7,10,21,26,20,20,16,32,4,28,18,10,15,7,25,5,15,6,32,27,21,7,19,20,27,11,6,33,27,1,24,7,6,15,23,17,32,7,21,29,13,28,28,16,33,27,9,22,29,4,15,26,22,22,1,16,28,32,15,16,12,31,33,24,2,28,22,11,17,3,15,6,1,5,7,4,24,8,3,26,21,23,10,10,6,8,23,14,2,13,28,25,13,8,15,12,18,24,8,17,21,3,5,10,22,5,13,28,4,23,24,30,20,13,4,15,16,11,7,5,23,9,9,8,20,14,20,18,8,13,16,19,24,27,26,17,6,29,7,11,13,14,16,18,13,30,17,27,16,10,29,9,23,13,29,32,25,33,32,13,27,27,22,12,3,12,1,28,10,15,3,3,13,29,11,4,17,23,26,5,31,8,15,26,29,12,31,31,15,11,6,18,29,8,33,24,21,10,21,24,15,16,4,7,9,24,28,21,5,1,28,21,1,7,5,4,22,9,15,20,10,23,8,24,26,2,26,7,17,16,10,29,30,10,24,20,25,13,10,4,14,23,13,18,14,4,23,26,6,25,23,33,9,11,23,30,2,5,13,28,1,4,6,27,2,10,14,15,13,17,12,8,26,5,6,13,15,20,6,8,31,18,8,19,28,22,24,13,9,33,5,16,32,26,3,21,30,27,14,15,7,14,4,18,2,11,20,33,17,9,8,18,9,14,16,29,23,14,15,27,1,2,9,30,1,28,14,26,15,16,33,8,10,17,3,19,1,12,22,23,25,24,31,6,31,19,19,4,13,33,7,5,11,23,23,8,31,24,11,24,29,19,11,29,18,26,2,23,3,33,18,3,7,1,33,17,14,23,7,3,10,21,9,23,30,27,31,19,15,18,26,25,23,9,24,10,19,13,14,2,26,11,22,32,23,6,27,33,22,13,26,21,26,30,24,2,10,12,15,27,29,7,24,19,19,33,4,28,13,10,29,4,29,26,25,9,13,28,22,13,2,26,15,10,10,10,1,26,3,32,23,32,26,29,5,12,32,13,8,12,19,28,7,6,5,29,15,14,14,2,13,17,5,32,28,8,26,32,21,27,21,28,20,2,12,26,28,21,21,29,23,22,18,31,21,6,24,3,23,8,3,2,18,31,22,19,31,22,9,20,15,16,25,16,11,8,18,21,11,32,7,16,9,19,30,5,30,12,13,18,16,7,32,29,4,28,25,13,13,25,1,6,11,31,26,18,5,24,30,6,9,30,3,1,8,12,20,9,12,8,27,3,6,6,9,14,22,29,2,10,31,31,1,28,21,30,20,14,29,24,11,21,14,5,21,8,1,6,9,25,14,20,13,33,9,10,2,18,21,29,27,8,25,4,30,27,16,7,5,33,8,27,2,12,2,3,13,3,4,14,2,24,27,3,30,19,10,26,7,6,3,12,19,1,15,15,32,21,30,11,6,6,17,9,1,20,31,1,18,27,9,6,15,2,18,25,24,28,20,8,16,20,7,3,7,29,18,2,9,1,29,32,29,12,15,8,33,19,31,29,25,10,8,12,3,4,4,10,9,18,7,28,3,14,26,27,20,4,4,9,11,1,16,27,1,3,7,15,25,26,13,4,6,7,28,2,7,3,31,2,16,1,19,27,10,21,32,1,4,16,12,12,24,5,11,22,19,3,18,21,5,24,3,6,30,17,17,2,2,13,2,26,32,29,21,28,12,14,2,18,22,14,20,13,14,25,2,17,12,9,18,22,2,30,30,31,31,20,13,26,25,18,15,11,17,24,33,13,1,16,26,33,2,5,24,3,23,17,13,17,10,30,23,26,12,21,10,11,13,23,4,28,19,28,17,15,10,6,1,3,29,9,9,17,29,3,12,14,20,24,7,5,1,1,3,28,12,2,4,14,22,18,27,17,22,31,23,8,22,17,1,5,23,17,17,30,3,12,33,28,32,31,22,4,33,25,4,12,20,6,5,25,18,15,10,16,10,32,7,32,3,10,2,26,2,14,21,19,26,9,3,5,6,31,32,22,3,30,32,1,22,1,10,12,5,3,33,6,8,11,15,33,18,14,11,20,15,10,7,32,28,12,2,22,1,29,29,2,7,26,27,25,24,20,4,32,1,4,26,5,4,14,32,32,20,25,20,5,19,16,12,20,6,28,7,10,25,15,3,26,22,6,25,17,13,14,2,13,19,17,7,12,7,15,19,2,1,14,13,16,25,19,26,24,25,11,32,7,23,30,25,16,7,19,26,9,33,12,9,19,20,31,15,5,29,14,29,27,13,10,17,23,25,14,27,30,21,12,10,25,15,8,24,26,3,28,10,8,18,33,23,9,10,3,27,23,28,33,20,16,21,13,9,33,26,27,26,16,15,16,31,29,22,6,4,28,3,23,27,6,2,14,29,25,4,28,18,24,20,21,13,12,10,24,19,16,18,31,19,30,28,26,14,5,15,5,11,6,30,7,21,21,7,27,26,12,23,32,19,5,2,15,32,18,1,1,28,14,18,31,4,19,4,31,27,17,7,22,10,5,16,14,1,18,2,21,1,29,22,2,33,28,16,18,19,14,26,30,9,27,31,24,7,26,1,9,18,27,30,17,26,5,6,33,13,4,14,4,16,29,30,22,28,28,6,9,28,17,22,24,2,25,4,1,1,11,29,12,23,19,18,27,1,19,18,22,21,4,20,32,31,10,13,25,22,25,14,19,18,10,12,21,7,2,12,28,29,4,11,22,15,6,28,25,9,11,29,20,13,26,24,4,17,4,10,32,25,1,30,16,2,29,11,23,7,28,12,13,20,26,3,10,21,2,11,32,13,5,16,27,5,25,2,1,1,15,10,24,3,20,31,2,22,2,27,1,4,2,2,23,27,9,32,4,10,2,20,8,13,13,28,25,33,16,4,30,26,6,8,19,32,3,24,15,13,30,33,22,21,16,30,23,7,30,17,19,6,8,31,17,6,25,19,2,14,30,16,32,6,31,3,7,5,26,11,31,25,5,25,26,33,12,29,18,11,25,21,3,4,17,5,20,26,10,19,10,17,30,11,29,8,5,23,2,1,23,20,27,3,14,13,7,23,31,27,14,6,21,3,13,11,32,30,13,19,24,25,30,14,4,6,9,11,29,21,21,12,19,23,9,22,26,30,15,29,7,32,13,28,31,30,25,33,12,31,8,18,11,5,13,16,24,18,8], 7333)
# print(ss)
# ss = s.numSubarrayProductLessThanK([4,32,23,1,11,21,8,3,12,21,33,5,14,11,9,14,4,27,5,7,7,14,13,9,17,10,3,4,17,31,7,19,4,7,20,5,4,3,24,30,9,11,23,16,7,21,23,22,12,20,8,20,18,11,5,8,21,5,11,31,28,21,13,21,22,3,2,1,32,8,8,27,4,26,13,14,4,15,6,10,28,15,18,20,29,1,1,12,5,18,10,9,5,13,1,2,7,3,23,26,3,4,13,9,32,32,31,26,19,8,7,29,16,21,28,14,18,5,25,3,4,33,27,3,10,10,22,13,13,32,18,11,27,12,3,33,21,3,5,23,12,23,23,20,24,31,26,7,25,1,5,28,1,1,29,7,31,20,21,32,23,24,13,21,14,30,8,5,23,26,31,31,25,33,17,30,20,20,16,16,2,8,10,5,10,16,27,8,25,5,3,22,21,30,25,20,4,10,9,4,3,20,14,13,4,3,3,1,32,29,13,25,13,28,10,26,17,29,13,28,20,22,6,6,2,30,15,2,29,21,10,28,33,22,6,25,8,18,29,17,1,25,17,27,27,28,16,18,3,4,5,28,20,32,11,23,1,33,12,7,29,32,6,33,15,33,24,13,32,15,24,20,11,27,20,7,2,21,6,11,16,27,24,22,7,4,15,16,1,25,22,16,4,9,19,16,10,14,9,30,18,17,6,8,9,23,1,9,22,20,5,1,15,30,23,3,8,10,9,22,24,9,24,9,5,20,27,16,22,7,6,11,22,27,31,16,30,8,14,12,9,2,29,33,13,18,14,30,20,19,16,33,8,31,31,30,6,15,6,2,30,15,32,17,33,14,22,2,4,23,22,21,29,8,31,26,28,26,20,12,12,18,1,20,17,8,10,10,4,5,7,28,8,31,13,11,31,17,27,27,25,10,8,30,12,17,24,19,16,31,28,15,28,17,16,7,16,1,23,7,25,11,5,19,3,1,14,10,29,19,17,29,20,20,24,5,1,29,29,14,16,2,7,29,15,14,18,14,20,4,9,30,8,28,30,18,18,15,20,6,5,2,29,3,1,29,3,6,12,16,20,27,6,5,30,14,3,9,16,15,28,2,11,22,16,12,9,15,10,22,18,13,29,31,26,31,33,21,13,20,20,12,33,15,22,7,31,24,21,21,30,7,25,31,28,25,19,8,27,27,16,31,17,12,20,30,23,15,21,1,6,10,28,10,27,31,24,9,3,23,8,30,31,2,19,8,31,3,16,30,32,1,9,9,10,30,29,12,28,20,32,22,33,2,1,18,33,32,16,9,5,21,27,29,14,6,6,21,13,23,18,15,29,21,32,29,4,9,5,33,22,7,11,17,24,10,13,4,10,1,3,11,8,12,20,18,11,8,2,25,6,25,18,1,1,21,19,11,5,2,12,7,20,20,2,31,14,26,16,15,22,6,27,6,10,20,20,31,20,13,20,12,24,15,16,23,18,3,22,22,8,20,3,5,20,16,11,11,28,2,2,32,18,28,12,32,12,27,26,30,29,4,1,22,14,7,12,23,31,11,18,7,25,12,8,24,9,14,17,25,16,4,3,29,22,17,25,17,26,22,22,19,28,2,17,24,19,18,26,9,4,25,23,15,25,23,24,29,20,18,13,22,11,9,24,12,14,6,1,22,1,21,21,8,13,15,8,29,13,2,8,17,8,27,14,6,9,29,25,31,3,10,22,30,11,19,4,12,10,6,21,27,16,22,8,32,13,6,19,30,29,26,22,2,11,8,28,17,19,10,11,19,33,23,15,12,32,31,20,5,16,11,16,4,13,24,26,18,33,14,30,33,24,19,33,19,12,27,24,29,33,13,14,10,22,25,24,32,18,5,9,6,33,27,31,26,12,16,7,30,3,12,25,11,12,28,31,5,32,13,1,5,3,26,11,25,9,28,16,3,27,13,19,18,16,12,15,18,9,4,25,6,16,14,2,10,20,22,20,20,8,7,7,5,32,30,9,27,33,22,4,13,8,6,11,18,18,27,26,27,25,15,22,16,11,13,15,25,11,29,7,3,15,26,21,27,22,29,11,16,2,25,32,24,17,11,13,15,9,33,31,14,20,22,32,4,25,13,28,33,4,9,16,20,22,6,23,7,18,30,9,12,19,32,27,33,5,22,18,9,9,6,5,5,4,4,33,16,13,5,28,24,24,6,1,14,13,12,15,10,24,22,12,10,31,33,29,24,18,18,13,25,26,32,15,3,14,14,26,19,32,15,33,33,2,6,10,24,21,21,31,31,12,22,12,6,30,32,8,16,24,26,13,13,16,5,17,26,4,4,7,27,27,5,14,24,23,32,13,3,23,10,30,23,31,30,18,25,11,24,21,7,19,13,19,4,28,22,27,2,17,12,33,32,4,25,21,23,24,7,13,21,33,7,33,31,7,20,30,13,22,19,33,16,2,20,4,31,2,31,21,12,24,23,22,2,20,19,15,2,28,4,9,30,15,13,30,4,17,24,13,32,2,12,24,24,19,11,19,6,33,2,9,26,25,16,15,24,6,15,4,28,2,3,32,18,10,2,13,24,16,13,28,28,22,33,25,21,2,5,2,21,1,8,17,2,5,18,33,29,27,20,30,27,23,25,1,8,19,33,22,30,17,24,17,7,16,16,4,25,23,4,31,12,10,30,17,17,14,4,24,10,32,13,14,15,29,17,13,7,4,21,16,23,16,2,13,12,33,23,27,33,28,15,31,25,13,12,20,14,18,18,7,31,3,31,30,33,13,6,26,13,14,33,26,4,17,13,7,15,5,18,19,24,25,15,14,33,19,26,19,16,27,20,12,6,11,6,5,17,29,17,10,25,26,10,6,8,25,5,11,11,7,32,14,2,2,32,25,12,30,20,32,18,30,19,20,30,31,11,21,13,27,22,15,9,26,4,10,4,9,2,5,5,31,14,26,32,8,30,19,16,27,6,4,12,17,18,24,13,17,16,4,5,30,11,21,21,21,4,25,26,13,2,13,2,8,32,6,12,32,9,30,15,24,11,7,26,14,10,10,22,13,28,2,21,20,19,16,1,14,16,1,26,8,3,14,4,20,1,3,21,26,25,20,1,18,17,6,16,8,17,30,24,32,9,4,24,8,23,12,28,4,32,5], 9931)
# print(ss)

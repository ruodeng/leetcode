from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        target_count = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                target_count += 1
        return target_count
        # hours.sort()
        # i=0
        # length = len(hours)
        # while i < length:
        #     if hours[i]>= target:
        #         return length-i
        #     if hours[length-1-i] < target:
        #         return i
        #     i+=1
        # return 0
hours = [0,1,2,3,4]
target = 2
s = Solution()
print(s.numberOfEmployeesWhoMetTarget(hours,target))

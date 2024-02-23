from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=[]
        arr.sort()
        i,j=0,1
        while j < len(arr):
            if arr[i] != arr[j]:
                if j-i in d:
                    return False
                d.append(j-i)
                i = j
            j+=1
        d.append(j-i)
        return len(d) == len(set(d))

        # d = {}
        # for i in arr:
        #     d[i] = d.get(i, 0) + 1
        # return len(d.values()) == len(set(d.values()))
s = Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3]))  # True
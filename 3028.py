class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        s = 0
        for n in nums:
            s+=n
            if s ==0:
                return 1
        return 0
class Solution:
    def firstBadVersion(self, n: int) -> int:
        i, j = 1, n
        while i < j:
            mid = (i + j) // 2
            if isBadVersion(mid):
                j = mid
            else:
                i = mid + 1
        return i
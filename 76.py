from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dictT = defaultdict(int)
        for c in t:
            dictT[c] += 1

        required = len(dictT)
        l,r = 0, 0
        windowCounts = defaultdict(int)
        formed = 0
        ans =[-1,0,0]
        while r < len(s):
            c = s[r]
            windowCounts[c] += 1

            if c in dictT and windowCounts[c]==dictT[c]:
                formed += 1
            while l <= r and formed == required:
                c = s[l]
                if ans[0] ==-1 or  r -l+1 < ans[0]:
                    ans = [r-l+1,l,r]
                windowCounts[c] -= 1
                if c in dictT and windowCounts[c] < dictT[c]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == -1 else s[ans[1]:ans[2] + 1]

s=Solution()
ss=s.minWindow("ADOBECODEBANC","ABC")
print(ss)

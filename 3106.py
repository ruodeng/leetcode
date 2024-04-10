class Solution:
    m=[]
    ans =[]
    s=""
    mins=""

    def getSmallestString(self, s: str, k: int) -> str:
        ss = [ord(x) for x in s]

        for i  in range(len(ss)):
            sss = ss[i]
            m = min(sss - 97, 123 - sss)
            q = k - m
            if q < 0:
                if k >0:
                    ss[i] = sss - k
                break
            else:
                k=q
                ss[i] = 97
        return ''.join([chr(x) for x in ss])

s = Solution()
print(s.getSmallestString("zbbz", 3))
print(s.getSmallestString("xaxcd", 4))
print(s.getSmallestString("lol", 0))
print(s.getSmallestString("g", 16))

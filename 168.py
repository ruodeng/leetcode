class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s=''
        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, i = divmod(columnNumber, 26)
            # print(columnNumber,i, chr(65+i))
            s=chr(65+i)+s
        return s


        # cn=[c for c in columnNumber]
        # ans,i=1,0
        # while len(cn) > 0:
        #     c = cn.pop()
        #     ans = ans  +  (ord(c) - 64) *  26**i
        #     i+=1
        # return ans-1
s = Solution()
# print(s.convertToTitle("AB"))
# print(s.convertToTitle("ZY"))
# print(s.convertToTitle("A"))

print(s.convertToTitle(2))
print(s.convertToTitle(28))
print(s.convertToTitle(701))
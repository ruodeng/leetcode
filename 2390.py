class Solution:
    def removeStars(self, s: str) -> str:
        ss=""
        # for c in s:
        #     if c!="*":
        #         ss+=c
        #     else:
        #         ss=ss[:-1]
        # return ss
        # count=0
        # for c in s[::-1]:
        #     if c =="*":
        #         count += 1
        #     elif count>0:
        #         count-=1
        #     else:
        #         ss+=c
        # return ss[::-1]
        st = []
        for ch in s:
            if ch == '*':
                st.pop()
            else:
                st.append(ch)
        return ''.join(st)

s = Solution()
print(s.removeStars("abc**def"))
print(s.removeStars("abc**def**ghi"))

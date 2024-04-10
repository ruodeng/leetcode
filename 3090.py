class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        m=0
        for i in range(len(s)):
            j=i
            dict={}
            f=False
            while j < len(s):
                dict[s[j]] = dict.get(s[j], 0) + 1
                if dict.get(s[j], 0)>2:
                    f=True
                    j += 1
                    break
                j += 1
            if f:
                m = max(m, j - i-1)
            else:
                m = max(m, j - i)

            # print(dict,i,j,m,f, s[i:j])
        return m
s=Solution()
print(s.maximumLengthSubstring("bcbbbcba"))
print(s.maximumLengthSubstring("aaaaa"))
print(s.maximumLengthSubstring("abaaa"))
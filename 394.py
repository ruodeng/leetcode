class Solution:
    def decodeString(self, s: str) -> str:
        if not s or not "[" in s:
            return s
        int_left,left,right,count,total, repeat_times=-1, -1,-1,0,0, 0
        for i in range(len(s)):
            if s[i]=="["  :
                if left == -1:
                    while int_left < i:
                        if s[int_left:i].isdigit():
                            repeat_times = int(s[int_left:i])
                            break
                        int_left+=1
                    left = i
                count+=1
                total+=1
            elif s[i]=="]":
                count-=1
                if count==0:
                    right=i
                    if total >1:
                        sub_string = self.decodeString(s[left+1:right])
                        return  s[:int_left]+repeat_times*sub_string+self.decodeString(s[right+1:])
                    else:
                        return  s[:int_left]+repeat_times*s[left+1:right]+self.decodeString(s[right+1:])

        return s
s = Solution()
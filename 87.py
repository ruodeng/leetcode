class Solution:
    mems={}
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        if sorted(s1) != sorted(s2):
            return False
        if len(s1) == 1:
            return False

        if (s1,s2) in self.mems:
            return self.mems[(s1,s2)]
        r = False
        for i in range(1,len(s1)):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                r=True
                break
            if self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i]):
                r=True
                break
        self.mems[(s1,s2)]=r
        return r

s=Solution()
print(s.isScramble("great","rgeat"))
print(s.isScramble("abcde","caebd"))

great>i
rgeat>j

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        for r in ransomNote:
            print(r, r in magazine)
            if r in magazine:
                magazine = magazine.replace(r, "", 1)
            else:
                return False
        return True

s = Solution()
# print(s.canConstruct("a","b"))
print(s.canConstruct("aa","ab"))
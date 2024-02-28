class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        for i in range(k):
            if s[i] in "aeiou":
                count+=1
        max_count=count
        for i in range(k,len(s)):
            if s[i] in "aeiou":
                count+=1
            if s[i-k] in "aeiou":
                count-=1
            max_count=max(max_count,count)
        return max_count
s = Solution()
print(s.maxVowels("abciiidef",3))

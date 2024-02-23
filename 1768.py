class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''.join([''.join(w) for w in zip(word1, word2)])
        if len(word1) > len(word2):
            s += word1[len(word2):]
        else:
            s += word2[len(word1):]
        return s

s = Solution()
print(s.mergeAlternately("abc", "pqr"))  # apbqcr
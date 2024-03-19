from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans=[]
        for word in words:
            for w in word.split(separator):
                if w:
                    ans.append(w)
        return ans
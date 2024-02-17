from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        maps = []
        for word in words:
            if len(word) >1:
                if word[0]   in maps and  word[:-1]   in maps:
                    maps.append(word)
            else:
                maps.append(word)
        maps.sort(key=lambda x: len(x), reverse=True)
        if len(maps) == 0:
            return ""
        return maps[0]







        # for i in range(len(words)-1, -1,-1):
        #     if len(words[i]) == 1:
        #         map.append(words[i])
        #     if len(words[i][:-1]) > 1 and words[i][:-1] not in words[:i]:
        #         return words[i]
        # print(words)



s = Solution()
# ss = s.longestWord(["w", "wo", "wor", "worl", "world"])
# print(ss)
# ss = s.longestWord(["a", "b", "banana", "apa", "app", "appl", "ap", "apply", "apple"])
# print(ss)
# ss = s.longestWord(["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"])
# print(ss)
ss = s.longestWord(["ogz","eyj","e","ey","hmn","v","hm","ogznkb","ogzn","hmnm","eyjuo","vuq","ogznk","og","eyjuoi","d"])
print(ss)

import collections
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        words_queue = {}
        words_len, sub_string_len = len(words), len(words[0])
        words_string_len = words_len * sub_string_len
        words.sort()
        i = 0
        words_dict = dict(sorted(collections.Counter(words).items(), key=lambda x: x[0]))

        # words_dict = collections.Counter(words)
        # sorted_words_dict = dict(sorted(words_dict.items()))
        has_init = False

        def find_substring(i):
            if not has_init:
                # ss =s[i:words_string_len + i]
                # print(ss)
                # for w in words:
                #     if w in ss:
                #         words_queue[w] = words_queue.get(w, 0) + 1
                #         ss.replace(w, "", 1)
                # for j in range(words_len):
                #     ss = s[ j * sub_string_len:  (j + 1) * sub_string_len]
                #     print(ss)
                #     if ss in words:
                #         # words.remove(ss)
                #         # words_queue.append(ss)
                #         words_queue[ss] = words_queue.get(ss, 0) + 1
                words_queue.clear()
                for j in range(words_len):
                    ss = s[i + j * sub_string_len:i + (j + 1) * sub_string_len]
                    if ss in words:
                        words_queue[ss] = words_queue.get(ss, 0) + 1
                    else:
                        break
            else:
                s_start = s[i - 1:i + sub_string_len - 1]
                s_end = s[i + (words_len - 1) * sub_string_len: i + words_len * sub_string_len]
                if s_start in words:
                    words_queue[s_start] = max(words_queue.get(s_start, 0) - 1, 0)
                if s_end in words:
                    words_queue[s_end] = words_queue.get(s_end, 0) + 1

        while i < len(s) - words_string_len + 1:
            find_substring(i)

            sorted_words_queue = dict(sorted(words_queue.items()))

            if words_dict == sorted_words_queue:
                # has_init = True
                ans.append(i)
            i += 1
        return ans


s = Solution()
# print(s.findSubstring("barfoothefoobarman", ["foo","bar"]))
# print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
# print(s.findSubstring("wordgoodgoodgoodbestword", ["good","good","word","best"]))
# print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
# print(s.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))
# print(s.findSubstring("barfoofoobarthefoobarman",["the","bar","foo"]))
# print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
# print(s.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))
# print(s.findSubstring("aaa", ["a", "a"]))
print(s.findSubstring("abaababbaba", ["ab","ba","ab","ba"]))

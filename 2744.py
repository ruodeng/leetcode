from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        dict,count= [],0
        for word in words:
            if word in dict:
                dict.remove(word)
                count+=1
            else:
                dict.append(word[::-1])
        return count
        # words_dicts_by_a_z={}
        # count = 0
        # for word in words:
        #     if word[1] in words_dicts_by_a_z and word[0] in words_dicts_by_a_z[word[1]]:
        #         count += 1
        #         words_dicts_by_a_z[word[1]][word[0]] -= 1
        #         if words_dicts_by_a_z[word[1]][word[0]] == 0:
        #             del words_dicts_by_a_z[word[1]][word[0]]
        #             if len(words_dicts_by_a_z[word[1]]) == 0:
        #                 del words_dicts_by_a_z[word[1]]
        #     else:
        #         if not word[0] in words_dicts_by_a_z:
        #             words_dicts_by_a_z[word[0]]={}
        #         if not word[1] in words_dicts_by_a_z[word[0]]:
        #             words_dicts_by_a_z[word[0]][word[1]]=1
        #         else:
        #             words_dicts_by_a_z[word[0]][word[1]]+=1
        # return count

s = Solution()
print(s.maximumNumberOfStringPairs(["ab","ba","cc"]))
words = ["cd","ac","dc","ca","zz"]
print(s.maximumNumberOfStringPairs(words))

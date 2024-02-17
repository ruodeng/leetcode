# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#
#         dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
#         dp[0][0] = True
#         for i in range(1, len(p) + 1):
#             flag = p[0] == "*"
#             for j in range(1, i):
#                 if p[j] != "*":
#                     flag = False
#                     break
#             dp[0][i] = flag
#
#         for i in range(1, len(s) + 1):
#             for j in range(1, len(p) + 1):
#                 if p[j - 1] == "*":
#                     dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
#                 elif p[j - 1] == "?" or s[i - 1] == p[j - 1]:
#                     dp[i][j] = dp[i - 1][j - 1]
#                 else:
#                     dp[i][j] = False
#         return dp[len(s)][len(p)]

class Solution:
    def isMatch(self, s: str, hehe: str) -> bool:
        i, lol, si, bruhh = 0, 0, -1, 0
        while i < len(s):
            if lol < len(hehe) and (s[i] == hehe[lol] or hehe[lol] == '?'):
                lol += 1
                i += 1
            elif lol < len(hehe) and hehe[lol] == '*':
                si = lol
                bruhh = i
                lol += 1
            elif si != -1:
                lol = si + 1
                bruhh += 1
                i = bruhh
            else:
                return False
        while lol < len(hehe) and hehe[lol] == '*':
            lol += 1
        return lol == len(hehe)

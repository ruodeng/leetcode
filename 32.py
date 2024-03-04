class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, max_length = [ ], 0
        for i in range(len(s)):
            if s[i] == ")" and stack and s[stack[-1]] == "(":
                stack.pop()
                max_length = max(max_length, i - (stack[-1] if stack else -1))
            else:
                stack.append(i)

            # if s[i] == "(":
            #     stack.append(i)
            # else:
            #     if stack and s[stack[-1]] == "(":
            #         stack.pop()
            #         max_length = max(max_length, i - (stack[-1] if stack else -1))
            #     else:
            #         stack.append(i)
        return  max_length
s = Solution()
# print(s.longestValidParentheses("(()"))
print(s.longestValidParentheses(")("))
print(s.longestValidParentheses(")()())"))
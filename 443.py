from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return len(chars)

        i = len(chars) - 1
        while i >= 0:
            j = i - 1
            while j >= -1 and chars[j] == chars[i]:
                j -= 1
            if j < -1:
                j = -1
            n = i - j
            if n > 1:
                for m in range(n-1):
                    chars.pop(j+1)
                while n > 0:
                    chars.insert(j+2, str(n % 10))
                    n = n // 10
                # chars.insert(j+2, str(n))
                # chars = chars[:i] + list(str(n)) + chars[i:]
            i = j
        print(chars)
        return len(chars)


s = Solution()
# print(s.compress(["a", "a", "b", "b", "c", "c", "c"]))
# print(s.compress(["a", "a", "b", "b", "c", "c", "c"]))
# print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
# print(s.compress([""]))
print(s.compress(["a","a"]))

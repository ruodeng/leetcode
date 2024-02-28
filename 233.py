from math import ceil


class Solution:
    def countDigitOne(self, n: int) -> int:
        num, i, s = n, 1, 0
        while num:
            if num % 10 == 0:
                s += (num // 10) * i
            if num % 10 == 1:
                s += (num // 10) * i + (n % i) + 1
            if num % 10 > 1:
                s += ceil(num / 10) * i
            num, i = num // 10, i * 10
        return s


s = Solution()
print(s.countDigitOne(13))
print(s.countDigitOne(113))

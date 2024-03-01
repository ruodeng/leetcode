
def guess(num: int) -> int:
    pass
class Solution:
    def guessNumber(self, n: int) -> int:
        small,big,middle=1,n,n//2
        while small <= big:
            r = guess(middle)
            if r == 0:
                return middle
            elif r == -1:
                big = middle -1
            else:
                small = middle +1
            middle = (big+small)//2

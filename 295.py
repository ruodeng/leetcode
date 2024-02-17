class MedianFinder:
    left = 0
    right = 0
    middle = 0
    count = 0
    even = False
    arr = []

    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        self.even = not self.even
        self.arr.append(num)
        if len(self.arr) > 2 and self.even:
            self.arr.remove(self.arr[0])
        if self.even:
            self.middle = num
        else:
            self.middle = (self.middle + num) / 2
        # 1   1
        # 1,2  1 2
        # 1,2,3   2
        # 1,2,3,8,  2,3
        # 1,2,3,8,9   3
        # 1,2,3,8,9,10  3,8
        #
        # 1
        # 1,2
        # 1,2,3
        # 1,2,3,8
        # 1,2,3,8,9

    def findMedian(self) -> float:
        self.arr.sort()
        if not self.even:
            return (self.arr[0] + self.arr[1]) / 2
        else:
            return self.arr[0]

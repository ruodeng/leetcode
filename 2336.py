class SmallestInfiniteSet:
    deleted= 0
    in_deleted=[]
    def __init__(self):
        # popSmallest() to 10, don't need record 1 to 10, just record 10 in self.deleted
        # and if addBack(1), then 1 is in self.in_deleted
        self.deleted = 0
        self.in_deleted=[]
    def popSmallest(self) -> int:
        if len(self.in_deleted) >0:
            m = min(self.in_deleted)
            self.in_deleted.remove(m)
            return m
        self.deleted += 1
        return self.deleted
    def addBack(self, num: int) -> None:
        if num == self.deleted:
            self.deleted -=1
            if num in self.in_deleted:
                self.in_deleted.remove(num)
        elif num < self.deleted:
            if num not in self.in_deleted:
                self.in_deleted.append(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()
param_1 = obj.popSmallest()
print(param_1)  # 1
param_1 = obj.popSmallest()
print(param_1)  # 2

obj.addBack(1)
param_1 = obj.popSmallest()
print(param_1)  # 4
param_1 = obj.popSmallest()
print(param_1)  # 5
param_1 = obj.popSmallest()
print(param_1)  # 6
obj.addBack(2)
obj.addBack(3)
param_1 = obj.popSmallest()
print(param_1)  # 5
param_1 = obj.popSmallest()
print(param_1)  # 6

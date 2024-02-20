import random


class RandomizedSet:
    arr = []
    ids={}

    def __init__(self):
        self.arr=[]
        self.ids= {}

    def find(self,val):
        if val in self.ids:
            return self.ids[val]
            # return self.ids.index(val)
        return -1


    def insert(self, val: int) -> bool:
        if self.find(val)!=-1:
            return False
        self.arr.append(val)
        self.ids[val]=len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        index=self.find(val)
        if index==-1:
            return False
        self.arr[index]=self.arr[-1]
        self.ids[self.arr[-1]]=index
        self.ids.pop(val)
        self.arr.pop()
        return True
    def getRandom(self) -> int:
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

s = RandomizedSet()
print(s.insert(1))  # True
print(s.remove(2))  # False
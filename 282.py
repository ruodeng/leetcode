from typing import List


class Solution:
    actionExec = ['+', '-', '*']
    actionType = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}

    def dfs(self, numInt:[int], target:int, operation:str, ops:List[str] = []):
        num=numInt.copy()
        operationOrigin = operation
        if len(num) == len(operation)+1:
            # print(operation)
            mulIndex = [i for i in range(len(operation)) if operation[i] == "*"]
            if mulIndex not in [None, []]:
                mulIndex.reverse()
                for i in mulIndex:
                    num[i] = num[i] * num[i + 1]
                    num.pop(i + 1)
                    operation = operation[:i] + operation[i + 1:]
            n=num[0]
            for i in range(len(operation)):
                n = self.actionType[operation[i]](n, num[i+1])
            if n == target:
                ops.append(operationOrigin)
            return

        for action in self.actionExec:
            self.dfs(num, target, operation + action, ops)

    def addOperators(self, num: str, target: int) -> List[str]:
        # numInt = [int(n) for n in num]
        numsInts=[]
        for step in range (1, len(num)+1):
            numInt =[]
            # for j in range(0, len(num), step):
                # rightIndex = min(j+step, len(num))
                # # print(j, step,j, rightIndex, num[step*j:rightIndex])
                # numInt.append(int(num[j:j+step]))

            for j in range(0, len(num)-step ):
                print(step,j)
                for k in range(0, j+1  ):
                    # if step==2:
                        # print(j,k, k+j, num[k+j:k+j+step])
                    numInt.append(int(num[k+j:k+j+step]))



            numsInts.append(numInt)

        # print(numsInts)




        # res = []
        # for  numInt in numsInts:
        #     self.dfs(numInt, target, '',res)
        #     nums = []
        #     for r in res:
        #         n = ''
        #         for i in range(len(r)):
        #             n += str(numInt[i]) + r[i]
        #         n += str(numInt[-1])
        #         nums.append(n)
        # return nums




s = Solution()
# ss = s.addOperators("123", 6)
# print(ss)

ss = s.addOperators("232", 8)
print(ss)
ss = s.addOperators("105", 5)
print(ss)

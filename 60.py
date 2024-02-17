import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:


        def render(path):
            nums = [i for i in range(1, n + 1)]
            newNums = []
            for p in path:
                if len(nums)<1:
                    break
                newNums.append(nums.pop(p))
            newNums.extend(nums)
            return ''.join([str(i) for i in newNums])


        nn, kk =n,k
        def dfs  (n, k, path, res):
            total =1
            for i in range(2, n ):
                total *= i
            current_order, rest_n = math.ceil(k/total), k % total

            if k == 1:
                # the first one
                return render(path)
            if k == 0:
                # the last one
                path.extend([-1 for _ in range(nn-len(path))])
                return render(path)

            if current_order < 1:
                path.append(0)
                return dfs (n-1, rest_n, path, res)
            else:
                path.append(current_order-1)
                return dfs (n-1, rest_n, path, res)
        return dfs (n, k, [], [])




s = Solution()
# ss = s.getPermutation(4,9)
# print("RE:",ss)
# ss = s.getPermutation(3,1)
# print("RE:",ss)
# ss = s.getPermutation(3,2)
# print("RE:",ss)
# ss = s.getPermutation(3,3)
# print("RE:",ss)
# ss = s.getPermutation(3,4)
# print("RE:",ss)
# ss = s.getPermutation(3,5)
# print("RE:",ss)
# ss = s.getPermutation(3,3)
# print(ss)
# ss = s.getPermutation(4,7)
# print(ss)
ss = s.getPermutation(4,2)
print(ss)
# ss = s.getPermutation(4,12)
# print(ss)
#
# ss = s.getPermutation(4,11)
# print(ss)



# 1//3 = 0
# 2//3 = 0
# 3//3 = 1
# 4//3 = 1
# 5//3 = 1
#
# 3%1 = 0
# 3%2 = 1
# 3%3 = 0
# 3%4 = 3
# 3%5 = 3
# 3%6 = 3
# 3%7 = 3


# 6//3 = 2
# 6//1 = 6
#
# 3//6 = 0
#
# 6
#
#
# 3,2,1
#
#
# 6//3 = 2
# 6//1 = 6
# 6%3 = 0
# 6%1 = 0
#
#
# 3//3 = 1
# 3%1 = 0
# 3%4 = 3
#
# 2%3 = 2
#
# 4//3 = 1
# 3%4 = 3
#
# 1 //2   = 0
# 1%2 = 1
#
# 5//3 = 1    3
# 2//2 = 1    12,21
# 2%2 = 0
#
# 6//3 = 2
# 3//2= 1
# 1//1 = 1
#
#
#
# 3//3 = 1
# 3%3 = 0
#
# 1//3 = 0
# 1%3 = 1
#
# # 4,9
# 4,3,2,1
#
# 9//4 = 2
# 9%4 = 1
#
# 5//3 = 1
# 5%3 = 2
#
# 2//2 = 1
# 2%2 = 0
#
#
# 3//3 = 1
#
#
#
# 1,2,3,4
#
# 9//4 = 2<3
# 9%4 = 1
# 5//3 = 1
# 5%3 = 2
# 2//2 = 1
# 2%2 = 0
#
#
# 123->231
#
#
# 4//3 = 1<2
# 4%3 = 1
#
# 4*3*2
# 24
# 4
# 6
#
# 4的话
# 24里第9个
# 24%9 = 6
# 24//9 = 2
#
# 6//2 = 3
# 6%2 = 0
#
# 3//0 第0个
#
#
# 123
# 6 4
#
# 6//4 = 1
# 6%4 = 2
#
# 2//2 = 1
# 2%2 = 0
#
#
#
#
#
#
# 123
# 132
#
# 213
# 231
#
# 312
# 321



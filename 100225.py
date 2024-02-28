from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        m=0
        for i in range(len(bottomLeft)- 1):
            for j in range(i+1,len(topRight)):
                k = [max(bottomLeft[j][0], bottomLeft[i][0]), max(bottomLeft[j][1], bottomLeft[i][1]),
                     min(topRight[j][0], topRight[i][0]), min(topRight[j][1], topRight[i][1])]
                l = min(k[2] - k[0], k[3] - k[1])
                print(i, j, k, l)
                if l > 0:
                    l*=l
                    if l > m :
                        m = l*l
                # x = topRight[i][0]-bottomLeft[j][0]
                # y = topRight[i][1]-bottomLeft[j][1]
                # if x>0 and y>0:
                #     k = [max(bottomLeft[j][0], bottomLeft[i][0]), max(bottomLeft[j][1], bottomLeft[i][1]),  min(topRight[j][0], topRight[i][0]), min(topRight[j][1], topRight[i][1])]
                #     l = min(k[2]-k[0], k[3]-k[1])
                #     print(i,j,k,l)
                #     if l>0:
                #         res.append(l*l)
        return m
        # res.sort()
        # if len(bottomLeft) == 2:
        #     return res[0] if res else 0
        # return res[-2] if res and len(res)>1  else 0


s = Solution()
print(s.largestSquareArea([[1,1],[2,2],[3,1]],[[3,3],[4,4],[6,6]]))
print(s.largestSquareArea([[1,1],[2,2],[1,2]],[[3,3],[4,4],[3,4]]))
print(s.largestSquareArea([[1,1],[3,3],[3,1]],[[2,2],[4,4],[4,2]]))
print(s.largestSquareArea([[1,2],[1,2]],[[4,5],[2,3]]))
print(s.largestSquareArea([[2,2],[3,1]],[[5,5],[5,5]]))
print(s.largestSquareArea([[2,4],[1,1]],[[4,5],[3,2]]))
print(s.largestSquareArea([[1,4],[1,1],[3,8]],[[6,9],[6,4],[8,10]]))
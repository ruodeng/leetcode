from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        i,j,high,high_index =0,1,ratings[0],0
        length = len(ratings)

        # i=0, j is high, if 2j+1 is slow, then 2j+1 is high
        while j < length:
            if ratings[j] > high:
                high = ratings[j]
                high_index = j
            elif ratings[j] < high:

            j+=1


        # 345654
        # 123421
        #
        # 121
        #
        # 124321
        # 123421
        # 12342123210


        while j < length:
            j+=1

        # def dfs(ratings,base):
        #     #find min and index
        #     min_rating = min(ratings)
        #     min_index = ratings.index(ratings)
        #     dfs(ratings[:min_index],base+1)   # * level
        #     if min_index < len(ratings)-1:
        #         dfs(ratings[min_index+1:],base+1)
        # dfs(ratings,1)

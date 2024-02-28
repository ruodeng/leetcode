from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        print("==================")
        print(ratings)
        left,right,high,high_index,low,low_index =0,1,ratings[0],0 ,ratings[0],0
        length = len(ratings)
        def find_high_or_low_func(right):
            if right == length:
                return -2
            if ratings[right] > ratings[right-1]:
                # find the high
                return 1
            elif ratings[right] < ratings[right-1]:
                # find the low
                return -1
            return 0
        peaks = []
        while left < length:
            find_high_or_low = find_high_or_low_func(  right)
            # print("::", left, right, ratings[left:right+1],find_high_or_low )
            while right <= length:
                find_high_or_low2 = find_high_or_low_func(  right)
                # print("====", left, right, length,ratings[left:right+1],find_high_or_low, find_high_or_low2)
                if find_high_or_low == find_high_or_low2  and right < length:
                    if find_high_or_low ==1 and  ratings[right] > high:
                        high = ratings[right]
                        high_index = right
                    elif find_high_or_low == -1 and ratings[right] < low:
                        low = ratings[right]
                        low_index = right
                    right += 1
                else:
                    count = right-1-left
                    # print(left, right-1, find_high_or_low,low,high)
                    # if not find_high_or_low2 == 0:
                    # find before until reverse
                    peaks.append(( count, find_high_or_low ))
                    # peaks.append((left, right-1, find_high_or_low,low,high))
                    break
            if right == length:
                # print(left, right-1, "END")
                # print(peaks, "END")
                break
            left=right-1
        print(peaks)
        total = 0
        for i in range(len(peaks)):
            if peaks[i][0] == 0:
                # TODO if 3,3,3,3
                continue
            if i == len(peaks) -1:
                count = peaks[i][0]
                total +=   count*(count+1)//2
            else:
                count = peaks[i][0]
                count2 = peaks[i+1][0]
                # TODO if 3,3,3,3,
                if count >= count2:
                    count+= 1
                else:
                    peaks[i+1]+=1
                total +=   count*(count+1)//2

            print('>>>>',peaks[i],total)
        print(total)


s = Solution()
print(s.candy([1,0,2]))  # 5
print(s.candy([1,2,2]))  # 4
print(s.candy([1,2,1]))  # 4
print(s.candy([1,0,2]))  # 5
print(s.candy([1,2,3,2]))  # 5
print(s.candy([1,2,3,3,3,2]))  # 5

1234321

# [1,0,2]
#
# min, high, min_index, high_index
# 1232101234321
# 123,3210,01234,321
# 12,3,21,0,123,4,321
# 2!,4!,5!,3!
#
# i=0,high_index=2,high=3,low_index=5,low=0
# 0,2,5,9,12
# 2-1=1, 5-2=3, 3 win
# 1,3,4,2
# 2,4,5,3
#
#
# 1,2,1
# 1,1
# 1!,2!
# 1,2,2
# 2!,2,
#
#
#
#
# find the min, find the second min
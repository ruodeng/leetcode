class Solution:
    def minimumOperations(self, num: str) -> int:
        first_zero=-1
        first_five=-1
        second_zero=-1
        second_five=-1
        length= len(num)
        for i in range(length-1, -1,-1):
            if second_zero > -1 and second_five > -1:
                break
            if first_zero == -1:
                if num[i] == "0":
                    first_zero = i
            else:
                if   second_zero == -1 and num[i] in ["5", "0"]:
                    second_zero = i
            if first_five == -1:
                if num[i] == "5":
                    first_five = i
            else:
                if num[i] in ["2", "7"] and second_five == -1:
                    second_five = i
        reduce = -2
        if first_zero > -1:
            reduce= second_zero
        if second_five > -1:
            reduce = second_five if second_five > reduce else reduce
        return length - reduce -2


s = Solution()
# ss = s.minimumOperations("2245330434")
# print(ss)
# ss = s.minimumOperations("2908305")
# print(ss)
# ss = s.minimumOperations("10")
# print(ss)
# ss = s.minimumOperations("251")
# print(ss)
ss = s.minimumOperations("1")
print(ss)
from typing import List


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        res = []
        mem={}
        def find(i, s, sub_arr):
            if len(s) == 0:
                return ""
            if s in mem:
                return mem[s]

            a = find(i,s[1:],sub_arr)
            b = find(i,s[:-1],sub_arr)
            # if "dz" in s:
            #     print(i, s,  a,"|", b, a > b)
            if a == "":
                if not b =="":
                    a=b
                else:
                    for sa in sub_arr:
                        if s in sa:
                            mem[s]=""
                            return ""
                    a=s
            else:
                if not b =="":
                    if len(a) > len(b):
                        a=b
                    elif len(a) == len(b) and a > b:
                        a=b
            mem[s]=a
            return a
        for i in range(len(arr)):
            res.append(find(i,arr[i], arr[:i]+arr[i+1:]))
        return res


        # "cab"
        # "ca"
        # "ab"


s= Solution()
arr = ["cab","ad","bad","c"]
print(s.shortestSubstrings(arr))
arr = ["abc", "bcd", "abcd"]
print(s.shortestSubstrings(arr))
arr = ["gfnt","xn","mdz","yfmr","fi","wwncn","hkdy"]
print(s.shortestSubstrings(arr))

arr = ["re","xzgn","kzppy","kml","ykzr","z","pauni","sorfv"]
print(s.shortestSubstrings(arr))



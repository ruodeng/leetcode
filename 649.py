import collections


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = 0, 0
        while len(senate) > 1:
            r_remain = collections.Counter(senate)["R"]
            if r_remain == 0:
                return "Dire"
            elif r_remain == len(senate):
                return "Radiant"
            res = []
            for i in range(len(senate)):
                if senate[i] == "R":
                    if d > 0:
                        d -= 1
                    else:
                        res.append("R")
                        r += 1
                else:
                    if r > 0:
                        r -= 1
                    else:
                        res.append("D")
                        d += 1
            senate = "".join(res)
        return "Radiant" if senate[0] == "R" else "Dire"
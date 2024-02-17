class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator == 0:
            return "0"
        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator//denominator))
        numerator %= denominator
        if numerator == 0:
            return "".join(res)
        res.append(".")
        dic = {}
        while numerator:
            if numerator in dic:
                res.insert(dic[numerator], "(")
                res.append(")")
                break
            dic[numerator] = len(res)
            numerator *= 10
            res.append(str(numerator//denominator))
            numerator %= denominator
        return "".join(res)
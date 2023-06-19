class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        result = 0
        while(a | b | c ):
            bitA = a & 1
            bitB = b & 1
            bitC = c & 1
            if bitA | bitB != bitC:
                if bitA & bitB:
                    result += 2
                else:
                    result += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return result
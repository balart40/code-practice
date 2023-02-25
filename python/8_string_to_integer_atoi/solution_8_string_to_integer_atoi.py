import math
import string


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        MAX = math.pow(2, 31) - 1
        MIN = -1 * math.pow(2, 31)
        s = s.strip()
        if s == "":
            return 0
        if (s[0] != "+" and s[0] != "-") and s[0] not in string.digits:
            return 0
        sign = 1
        if s[0] == "-":
            s = s[1:]
            sign = -1
        elif s[0] == "+":
            s = s[1:]
            sign = 1
        result = ""
        for i in range(len(s)):
            if s[i] == " " or s[i] == "+" or s[i] == "-" or s[i] not in string.digits:
                break
            if s[i] in string.digits:
                result += s[i]
        if len(result) == 0 or result == "":
            return 0
        result = int(result * sign)
        if MIN <= result <= MAX:
            return int(result)
        elif result < MIN:
            return int(MIN)
        else:
            return int(MAX)


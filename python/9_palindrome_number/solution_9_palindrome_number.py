import math


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if len(str(x)) == 1:
            return True

        def isStrPalindrome(s):
            n = len(s)
            idx = 0
            if n % 2 == 0:
                idx = n/2
            else:
                idx = int(math.floor(n/2))
            idx -= 1
            i = 0
            while i <= idx:
                if s[i] != s[-1-i]:
                    return False
                i +=1
            return True

        return isStrPalindrome(str(x))

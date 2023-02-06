import math
import string


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        modRes = n % 2
        s = s.replace(" ", "")
        for char in string.punctuation:
            if char in s:
                s = s.replace(char, "")
        n = len(s)
        if modRes:
            idx = math.floor(n/2)
        else:
            idx = n/2 - 1
        i = 0
        s = s.lower()
        if s == "":
            return True
        while i <= idx:
            if not s[i] == s[n-1-i]:
                return False
            i += 1
        return True

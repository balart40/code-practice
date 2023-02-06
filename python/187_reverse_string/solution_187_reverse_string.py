import math


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        modRes = n % 2
        if modRes:
            idx = math.floor(n/2)
        else:
            idx = n/2 - 1
        i = 0
        while i <= idx:
            s[i], s[n-1-i] = s[n-1-i], s[i]
            i += 1
        # comment this in leetcode
        return s

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True
        if t == "":
            return False
        i = 0
        j = 0
        while i < len(s):
            if j >= len(t):
                return False
            if s[i] == t[j]:
                if i == len(s) - 1:
                    return True
                i += 1
            j += 1


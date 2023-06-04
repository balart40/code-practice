class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True
        pointer_s = 0
        pointer_t = 0
        ns = len(s)
        nt = len(t)
        while pointer_s < ns and pointer_t < nt:
            if t[pointer_t] ==  s[pointer_s]:
                pointer_s += 1
            pointer_t += 1
        return pointer_s == ns
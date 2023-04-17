class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return 0
        curr_len = 1
        prev_len = 0
        count = 0
        for i in range(1, n):
            if s[i] ==  s[i-1]:
                curr_len += 1
            else:
                prev_len =  curr_len
                curr_len = 1
            if prev_len >= curr_len:
                count += 1
        return count
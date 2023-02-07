import math
import string


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        s = s.strip(" ").split(' ')[::-1]
        i = 0
        while i < len(s):
            if s[i] == "" or s[i] == " ":
                s.pop(i)
                i -= 1
            i += 1
        for i in range(len(s)):
            s[i] = s[i].strip()
        s = string.join(s, " ")
        return s
        '''
        return " ".join(reversed(s.split()))





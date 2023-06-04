class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip().split(" ")[::-1]
        s_reversed_word = ""
        for i in range(len(s)):
            if s[i]:
                if i != len(s) - 1:
                    s_reversed_word += s[i] + " "
                else:
                    s_reversed_word += s[i]
        return s_reversed_word
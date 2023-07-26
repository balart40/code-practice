class Solution(object):
    def minWindow(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: str
        """
        window = ""
        left = -1
        while True:
            for char in s2:
                left = s1.find(char, left + 1)
                if left ==  -1:
                    return window
            right = left
            left += 1
            for char in reversed(s2):
                left = s1.rfind(char, 0, left)
            if not window or len(window) > right - left + 1:
                window = s1[left:right + 1]
            left += 1
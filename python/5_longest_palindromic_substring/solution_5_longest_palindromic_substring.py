class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def findLongestPalindrome(s, left,right):
            while left >= 0 and right < len(s) and s[left]==s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        def retunLongest(s1, s2):
            return s1 if len(s1) > len(s2) else s2

        n = len(s)
        res  = ""
        for i in range(n):
            # res = max(findLongestPalindrome(s, i, i), findLongestPalindrome(s, i, i+1), res, key=len)
            temp = findLongestPalindrome(s, i, i)
            res = retunLongest(temp, res)
            temp = findLongestPalindrome(s, i, i+1)
            res = retunLongest(temp, res)
        return res

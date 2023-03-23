class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tempDict = dict()
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        l_ptr = 0
        maxSubarrayLen = 0
        for r_ptr in range(len(s)):
            while tempDict.get(s[r_ptr], None) != None:
                del tempDict[s[l_ptr]]
                l_ptr += 1
            tempDict[s[r_ptr]] =  s[r_ptr]
            maxSubarrayLen = max(maxSubarrayLen, r_ptr - l_ptr + 1)
        return maxSubarrayLen
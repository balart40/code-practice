class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        left = right = max_length = 0
        for i in range(n):
            if s[i] ==  "(":
                left += 1
            elif s[i] == ")":
                right += 1
            if right == left:
                max_length =  max(max_length, left*2)
            elif right > left:
                right = left = 0
        left = right = 0
        for i in range(n-1, -1, -1):
            if s[i] ==  "(":
                left += 1
            elif s[i] == ")":
                right += 1
            if right == left:
                max_length =  max(max_length, left*2)
            elif left > right:
                right = left = 0
        return max_length
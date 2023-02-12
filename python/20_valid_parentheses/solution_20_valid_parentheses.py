class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        n = len(s)
        balanced = 0
        if n == 1 or s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False
        for i in range(n):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.insert(0, s[i])
                balanced += 1
            elif stack == []:
                return False
            elif s[i] == ")":
                if stack.pop(0) != "(":
                    return False
                balanced -= 1
            elif s[i] == "]":
                if stack.pop(0) != "[":
                    return False
                balanced -= 1
            elif s[i] == "}":
                if stack.pop(0) != "{":
                    return False
                balanced -= 1
        return balanced == 0

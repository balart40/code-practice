import collections


class Solution:
    def isValid(self, s: str) -> bool:
        d = { "}" : "{", ")" : "(", "]" : "["}
        queue = collections.deque()
        for i in range(len(s)):
            if s[i] == "{" or s[i] == "(" or s[i]  == "[":
                queue.append(s[i])
            elif not queue or d[s[i]] != queue.pop():
                return False
        return True if not queue else False
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a":"a","e":"e","i":"i","o":"o","u":"u","A":"A","E":"E","I":"I","O":"O","U":"U"}
        stack = []
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[i] in vowels:
                stack.append(s[i])
        result = ""
        for i in range(n):
            if s[i] in vowels:
                result += stack.pop(0)
            else:
                result += s[i]
        return result
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        counter = 0
        n = len(s)
        d = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True, 'A': True, 'E': True, 'I': True, 'O': True, 'U': True}
        for i in range(n):
            if i < n // 2 and d.get(s[i], False):
                counter += 1
            elif i > n // 2 - 1 and d.get(s[i], False):
                counter -= 1
        return True if counter == 0 else False
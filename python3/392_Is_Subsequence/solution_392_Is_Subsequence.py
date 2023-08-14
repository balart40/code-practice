class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)
        pointer_s = 0
        if ns == 0:
            return True
        for pointer_t in range(nt):
            if t[pointer_t] == s[pointer_s]:
                pointer_s += 1
                if pointer_s == ns:
                    return True
        return False

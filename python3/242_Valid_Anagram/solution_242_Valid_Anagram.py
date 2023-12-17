class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = collections.defaultdict(int)
        for char in s: d[char] += 1
        for char in t:
            if char not in d:
                return False
            d[char] -= 1
            if d[char] < 0: return False
        return True if sum(d.values()) == 0 else False
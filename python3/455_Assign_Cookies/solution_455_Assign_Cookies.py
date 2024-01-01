class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count, j = 0, 0
        while(count < len(g) and j < len(s)):
            if g[count] <= s[j]:
                count += 1
            j += 1
        return count
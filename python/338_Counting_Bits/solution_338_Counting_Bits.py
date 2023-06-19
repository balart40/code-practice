class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n+1):
            ones = bin(i)[2:].count('1')
            result.append(ones)
        return result
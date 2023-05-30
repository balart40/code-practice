class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result =  []
        start = 0
        if n == 1:
            result.append(0)
            return result

        if n % 2 != 0:
            result.append(0)

        start = 1
        while len(result) < n:
            result.insert(0, -1 * start)
            result.append(start)
            start += 1
        return result
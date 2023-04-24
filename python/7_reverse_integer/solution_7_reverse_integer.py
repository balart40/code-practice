class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        minInt = -1 * 2 ** 31
        maxInt = -1 * minInt -1
        sign = ""
        curr = ""
        if x < 0:
            sign = "-"
        curr = (str(x)).replace("-","")
        curr = sign+curr[::-1]
        curr = int(curr)
        return curr if minInt <= curr <= maxInt else 0
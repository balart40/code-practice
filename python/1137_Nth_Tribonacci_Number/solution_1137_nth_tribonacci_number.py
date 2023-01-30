class Solution_1137_nth_tribonacci_number:
    def __init__(self):
        pass

    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        nt_minus_three = 0
        nt_minus_two = 1
        nt_minus_one = 1
        result = 0
        if n == 0:
            return nt_minus_three
        if n == 1:
            return nt_minus_two
        if n == 2:
            return nt_minus_one
        else:
            for i in range(3, n+1):
                result = nt_minus_one + nt_minus_two + nt_minus_three
                nt_minus_three = nt_minus_two
                nt_minus_two = nt_minus_one
                nt_minus_one = result
            return result

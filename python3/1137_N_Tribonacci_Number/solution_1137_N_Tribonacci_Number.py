class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        n_minus_three = 0
        n_minus_two = 1
        n_minus_one = 1
        current = 0
        for i in range(3, n + 1):
            current = n_minus_one + n_minus_two + n_minus_three
            n_minus_three = n_minus_two
            n_minus_two = n_minus_one
            n_minus_one = current
        return current
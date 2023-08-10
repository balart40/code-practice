class Solution:

    def count_ways_to_eat(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0
        return self.count_ways_to_eat(n - 1) + self.count_ways_to_eat(n - 2) + self.count_ways_to_eat(n - 3)
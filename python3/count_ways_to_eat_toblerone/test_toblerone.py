import unittest
from solution_count_ways_to_eat_toblerone import Solution


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        n = 5
        solution = Solution()
        expected = 13
        self.assertEqual(expected, solution.count_ways_to_eat(n))

if __name__ == '__main__':
    unittest.main()

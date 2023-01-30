import unittest
from solution_1137_nth_tribonacci_number import Solution_1137_nth_tribonacci_number

class MyTestCase(unittest.TestCase):
    def test_for_n_four(self):
        expected_for_n_four = 4
        int_input = 4
        solution = Solution_1137_nth_tribonacci_number()
        self.assertEqual(expected_for_n_four, solution.tribonacci(int_input), "expected answer for n=4 is: 4")

    def test_for_n_25(self):
        expected_for_n_four = 1389537
        int_input = 25
        solution = Solution_1137_nth_tribonacci_number()
        self.assertEqual(expected_for_n_four, solution.tribonacci(int_input), "expected answer for n=25 is: 1389537")

if __name__ == '__main__':
    unittest.main()

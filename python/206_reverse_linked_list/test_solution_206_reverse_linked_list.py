import unittest
from solution_206_reverse_linked_list import Solution


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyTestCase(unittest.TestCase):
    def test_something(self):
        two = ListNode(2, None)
        one = ListNode(1, two)
        solution = Solution()
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

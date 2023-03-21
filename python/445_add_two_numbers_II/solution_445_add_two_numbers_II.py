# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # solution with strings to workaround carry mngmnt
        first = ""
        second = ""
        # get numbers in str
        while l1 != None or l2 != None:
            if l1:
                first += str(l1.val)
                l1 = l1.next
            if l2:
                second += str(l2.val)
                l2 = l2.next
        # get result
        resultInt = int(first) + int(second)
        # generate to list
        resultInt = [int(x) for x in str(resultInt)]
        result = curr = ListNode(0)
        for i in range(len(resultInt)):
            curr.next = ListNode(resultInt[i])
            curr = curr.next
        return result.next